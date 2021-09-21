# Basic working of a Neuron in a Neural Network.
# Every neuron has a unique connection to every single previous neuron,
# that serves as it's inputs.
# This is now a neuron in the output layer, with 4 previous neurons connected to it.

# You can never change inputs values directly. But, they can be be changed by changing their weights
# and bias. This is how you tune the model.
# This will be the output from the 4 previous neurons, just their weights and bias will change.
inputs = [1, 2, 3, 2.5]
# Every input has it's own unique weight.
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

# Each neuron just has one bias.
bias1 = 2
bias2 = 3
bias3 = 0.5

output = [
    inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
    inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
    inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3
]
print(output)
