import onnx
import onnx.helper as oh

# Define inputs and outputs with explicit shapes
input_a = oh.make_tensor_value_info("X_0", onnx.TensorProto.FLOAT, [1])
input_b = oh.make_tensor_value_info("X_1", onnx.TensorProto.FLOAT, [1])
output_y = oh.make_tensor_value_info("Y_0", onnx.TensorProto.FLOAT, [1])

# Add node
add_node = oh.make_node("Add", ["X_0", "X_1"], ["Y_0"])

# Create graph
graph = oh.make_graph(
    nodes=[add_node],
    name="AdditionModel",
    inputs=[input_a, input_b],
    outputs=[output_y]
)

# Set model version and create model
model = oh.make_model(graph, producer_name="simple-add")
model.opset_import[0].version = 11  # Set opset version

# Check the model
onnx.checker.check_model(model)

# Save model
onnx.save(model, "add.onnx")
print("ONNX model saved successfully")

# Verify the model
model_loaded = onnx.load("add.onnx")
print("\nModel verification:")
print("Inputs:")
for i, inp in enumerate(model_loaded.graph.input):
    print(f"  {i}: {inp.name} - {inp.type}")

print("Outputs:")
for i, outp in enumerate(model_loaded.graph.output):
    print(f"  {i}: {outp.name} - {outp.type}")

print("Nodes:")
for node in model_loaded.graph.node:
    print(f"  {node.op_type}: {node.input} -> {node.output}")