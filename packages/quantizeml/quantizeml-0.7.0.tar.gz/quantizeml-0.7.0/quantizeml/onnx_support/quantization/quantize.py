from pathlib import Path
import tempfile
from collections import namedtuple
import onnx
from onnxruntime.quantization.quant_utils import load_model
from .calibration import calibrate
from .input_scale import needs_zp
from ..graph_tools import nodes_to_ops_list, infer_partial_io
from .. import layers as onnx_qlayer
from ..layers.base_layer import get_brainchip_opsetid
from ..layers.sanitize import sanitize
from .data_reader import CalibrationDataReader
from ...layers.quantization_params import QuantizationParams

# Define named tuples for QuantizerPattern and Quantizer
QuantizePattern = namedtuple('QuantizerPattern', ['pattern', 'f'])
Quantizer = namedtuple('Quantizer', ['qlayer', 'input_ids', 'out_ranges'])

# List of supported patterns, together with matching function
PATTERNS_MAP = [
    QuantizePattern(["Conv", "Relu", "GlobalAveragePool"], onnx_qlayer.get_qconv),
    QuantizePattern(["Conv", "Relu", "MaxPool"], onnx_qlayer.get_qconv),
    QuantizePattern(["Conv", "GlobalAveragePool"], onnx_qlayer.get_qconv),
    QuantizePattern(["Conv", "Relu"], onnx_qlayer.get_qconv),
    QuantizePattern(["Conv"], onnx_qlayer.get_qconv),
    QuantizePattern(["DepthwiseConv", "Relu"], onnx_qlayer.get_qdepthwise),
    QuantizePattern(["DepthwiseConv"], onnx_qlayer.get_qdepthwise),
    QuantizePattern(["Flatten", "Gemm", "Relu"], onnx_qlayer.get_qgemm),
    QuantizePattern(["Flatten", "Gemm"], onnx_qlayer.get_qgemm),
    QuantizePattern(["Gemm", "Relu"], onnx_qlayer.get_qgemm),
    QuantizePattern(["Gemm"], onnx_qlayer.get_qgemm),
    QuantizePattern(["Add"], onnx_qlayer.get_qadd),
]


def add_quantizer(tensor_range, graph):
    input_ts = graph.input[0]
    input_name = input_ts.name
    input_unsigned = needs_zp(graph)
    input_range = tensor_range[input_name]
    quantizer = onnx_qlayer.InputQuantizer(name="quantize",
                                           input_tp=input_ts,
                                           input_signed=not input_unsigned)
    return quantizer, input_range


def build_model(nodes, weights, input_vinfo, output_vinfo):
    """
    Given a list of nodes, weights, input value info and output value info,
    create a model and return it.

    Args:
        nodes: list of nodes
        weights: list of weights
        input_vinfo: input value info
        output_vinfo: output value info

    Returns:
        model: onnx model build from given data
    """
    graph = onnx.helper.make_graph(nodes,
                                   "quantized_model",
                                   input_vinfo,
                                   output_vinfo,
                                   initializer=weights)
    # TODO: modify this so it fills it with opset_imports from nodes
    opset_imports = [get_brainchip_opsetid(), onnx.helper.make_opsetid(
        "", onnx.defs.onnx_opset_version())]
    # Add used functions to model
    functions = []
    node_op_list = nodes_to_ops_list(nodes)
    for func in onnx_qlayer.AKIDA_ONNX_LAYERS:
        if func.name in node_op_list and func not in functions:
            functions.append(func)
    # Build final model
    model = onnx.helper.make_model(graph, functions=functions, opset_imports=opset_imports)
    return model


def quantize_calibrated(target_model, tensors_range):
    """
    Given a calibrated onnx model and associated tensor ranges, create a quantized onnx
    model compatible with Brainchip's Akida IP and returns it as a new onnx model.

    Args:
        target_model: file path of model to quantize
        tensors_range: dictionary of tensor name and its range.
            Range is a tuple of min and max values.
            Example: {"input_0": (-1.23, +4.56)}

    Returns:
        quantized onnx model.
    """
    # Reject multi-input-output models (yet)
    if len(target_model.graph.input) != 1 or len(target_model.graph.output) != 1:
        raise RuntimeError("Only single input/output models are supported.")

    # Sanitize the model and make it quantization ready
    model = sanitize(target_model)

    graph = model.graph
    nodes = list(graph.node)
    ops_list = nodes_to_ops_list(nodes)

    # Add quantizer at the beginning of the model
    qlayer, input_range = add_quantizer(tensors_range, graph)
    quantizers = [Quantizer(qlayer, [], input_range)]

    # Split in blocks.
    remaining_nodes = list(target_model.graph.node)
    output_names = [target_model.graph.input[0].name]
    i = 0
    while i < len(ops_list):
        pattern_found = False
        for qpattern in PATTERNS_MAP:
            pattern = qpattern.pattern
            pat_len = len(pattern)
            if ops_list[i:i + pat_len] == pattern:
                pattern_found = True
                # Find to which quantized node the block is connected
                input_ids = [output_names.index(x) for x in nodes[i].input if x in output_names]
                # Initialize quantized layer
                block_nodes = nodes[i:i + pat_len]
                qlayer = qpattern.f(block_nodes, graph)
                # Recover calibration ranges
                out_ranges = tensors_range[block_nodes[-1].output[0]]
                # Create intermediate Quantizer representation
                quantizer = Quantizer(qlayer, input_ids, out_ranges)
                quantizers.append(quantizer)
                i += pat_len
                output_names.append(nodes[i - 1].output[0])
                # Remove nodes to be quantized from target model
                while len(remaining_nodes):
                    node = remaining_nodes.pop(0)
                    if node.output[0] == nodes[i - 1].output[0]:
                        break
                break
        if not pattern_found:
            break

    if i == 0:
        raise RuntimeError("No quantizable pattern found")

    # Now create quantized nodes
    qnodes = []
    weights = []

    # Main loop: quantize qlayers and concatenate them in qnodes
    conv_layers = (onnx_qlayer.QuantizedConv2D, onnx_qlayer.QuantizedDepthwise2D)
    for qidx, quantizer in enumerate(quantizers):
        last_quantizer = quantizer == quantizers[-1]
        # Note downscale is just implemented for QuantizedAdd and QuantizedDense1D
        downscale = not last_quantizer or isinstance(quantizer.qlayer, conv_layers)
        # QuantizedAdd constraint: power-of-two input scales are mandatory.
        # In other words, we force output scale to be a power-of-two if next layer is
        # a QuantizedAdd.
        force_fp = False
        for q in quantizers[qidx + 1:]:
            if qidx in q.input_ids and qidx < len(quantizers):
                force_fp = isinstance(q.qlayer, onnx_qlayer.QuantizedAdd)
                break
        # Recover input layers
        qinputs = [quantizers[iid].qlayer for iid in quantizer.input_ids]
        qnode, onnx_weights = quantizer.qlayer.quantize(*qinputs,
                                                        out_tensor_range=quantizer.out_ranges,
                                                        force_fp=force_fp,
                                                        downscale=downscale)
        qnodes.append(qnode)
        weights += onnx_weights

    # Build remaining float graph (nodes whose pattern does not exist)
    remaining_float_weights = sum([list(x.input) for x in remaining_nodes], [])
    remaining_weights = [w for w in graph.initializer if w.name in remaining_float_weights]
    partial_float_in, _ = infer_partial_io(remaining_nodes, [x.name for x in remaining_weights])
    remaining_input = []
    for out_name in partial_float_in:
        remaining_input.append(onnx.helper.make_tensor_value_info(out_name,
                                                                  elem_type=onnx.TensorProto.FLOAT,
                                                                  shape=None))
    remaining_model = build_model(remaining_nodes, remaining_weights, remaining_input, graph.output)
    if len(remaining_nodes) == 0:
        # Output needs to be dequantized when there are no remaining_nodes
        remaining_model.graph.input.extend(graph.output)

    # Plug a dequantizer per each remaining input
    deq_output_info, io_deq_map = [], []
    for input_value_info in remaining_model.graph.input:
        iname = input_value_info.name
        qlayer = quantizers[output_names.index(iname)].qlayer
        deq = onnx_qlayer.Dequantizer(name=f"{qlayer.output.name}/dequantize")
        qnode, onnx_weights = deq.quantize(qlayer)
        qnodes.append(qnode)
        weights += onnx_weights
        # Create output value info
        deq_output_info.append(deq.output)
        # Save input output map
        io_deq_map.append((deq.output.name, iname))

    # Finally build the quantized model
    qmodel = build_model(qnodes, weights, graph.input, deq_output_info)
    if len(remaining_nodes) > 0:
        # Note: we would use onnx.compose helper tool to merge the models manually,
        # avoiding somes issues (e.g. topological ordering).
        qmodel = onnx.compose.merge_models(qmodel, remaining_model, io_map=io_deq_map)
    return qmodel


def quantize(model_input,
             qparams=QuantizationParams(),
             samples=None,
             num_samples=1024,
             batch_size=None):
    """
    Given an onnx model and calibration data reader, create a quantized onnx
    model compatible with Brainchip's Akida IP and returns it as a new onnx model.

    Args:

        model_input (ModelProto): the onnx model instance to quantize
        qparams (QuantizationParams, optional): Quantization parameters. It is used
            to determine if quantizing per-tensor or per-axis.
        samples (list of numpy arrays, optional): List of input samples to use for
            calibration. If not provided, random samples will be generated. Defaults
            to None.
        num_samples (int, optional): Number of samples to use for calibration.
            Defaults to 1024.
        batch_size (int, optional): Batch size to use for calibration. Defaults to
            None.

    Returns:
        quantized onnx model.
    """
    # For now only a limited QuantizationParams configuration is supported: test that
    if (
            qparams.activation_bits != 8 or
            qparams.buffer_bits != 32 or
            qparams.input_weight_bits != 8 or
            qparams.output_bits != 8 or
            qparams.weight_bits != 8):
        raise ValueError("Only default bitwidth params params qparams is allowed.")

    with tempfile.TemporaryDirectory(prefix="pre.quant.") as quant_tmp_dir:
        # To perfom ONNXRuntime optimization, we would like to use
        # onnxruntime.quantization.load_model, to optimize the model (when required)
        # and infer the intermediate shapes.
        # However, it always expects to read the model from a path. That is why we
        # save the input model if it is not a path.
        onnx.save_model(model_input, f"{quant_tmp_dir}/model.onnx")
        model_input = f"{quant_tmp_dir}/model.onnx"

        # Perform preprocessing
        model = load_model(Path(model_input), need_optimize=True)

    # Compute statistical ranges
    # Create a calibration data reader from given samples.
    calibration_data_reader = CalibrationDataReader(model, samples, num_samples, batch_size)
    tensors_range = calibrate(model,
                              calibration_data_reader,
                              per_tensor_activations=qparams.per_tensor_activations)

    qmodel = quantize_calibrated(model, tensors_range)
    return qmodel
