# Basic working of a Neuron in a Neural Network
# Every neuron has a unique connection to every single previous neuron,
# That serves as it's inputs.
# In this case the neuron is connected to 3 previous neurons.
inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = (inputs[0]*weights[0]) + (inputs[1]*weights[1]) + (inputs[2]*weights[2]) + bias
print(output)