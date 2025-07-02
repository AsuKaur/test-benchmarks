
import onnx
import onnx.helper as oh

# Define inputs and outputs
a = oh.make_tensor_value_info("X_0", onnx.TensorProto.FLOAT, [1])
b = oh.make_tensor_value_info("X_1", onnx.TensorProto.FLOAT, [1])
z = oh.make_tensor_value_info("Y_0", onnx.TensorProto.FLOAT, [1])

# Nodes: Sub and ReLU
sub_node = oh.make_node("Sub", ["X_0", "X_1"], ["X_2"])
relu_node = oh.make_node("Relu", ["X_2"], ["Y_0"])

# Graph
graph = oh.make_graph(
    nodes=[sub_node, relu_node],
    name="ReluSubModel",
    inputs=[a, b],
    outputs=[z]
)

# Model
model = oh.make_model(graph, producer_name="sub-relu")


# Check the model
onnx.checker.check_model(model)

onnx.save(model, "sub_relu.onnx")
print("✅ Saved ONNX model")
