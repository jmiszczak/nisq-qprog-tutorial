import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pennylane as qml
import pennylane.qaoa as qaoa

# start with a graph
edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
graph = nx.Graph(edges)

#nx.draw(graph, with_labels=True)
#plt.show()

# cost and mixer is given from pennylane
cost_h, mixer_h = qaoa.min_vertex_cover(graph, constrained=False)
print ('Cost Hamiltonian', cost_h)
print ('Mixer Hamiltonian', mixer_h)

# QAOA with two parameters
def qaoa_layer(gamma, alpha):
    qaoa.cost_layer(gamma, cost_h)
    qaoa.mixer_layer(alpha, mixer_h)

# full circuit
wires = range(4)
depth = 2

# initial state and QAOA
def circuit(params, **kwargs):
    for w in wires:
        qml.Hadamard(wires=w)
    qml.layer(qaoa_layer, depth, params[0], params[1])

# device used as a backend
dev = qml.device("qulacs.simulator", wires=wires)

# cost function - expectation of cost_h on the device
cost_function = qml.ExpvalCost(circuit, cost_h, dev)

# optimization loop
optimizer = qml.GradientDescentOptimizer()
steps = 20
params = [[0.5, 0.5], [0.5, 0.5]]

for i in range(steps):
    params = optimizer.step(cost_function, params)

print("Optimal parameters")
print(params)

@qml.qnode(dev)
def prob_circuit(gamma, alpha):
    circuit([gamma, alpha])
    return qml.probs(wires=wires)

probs = prob_circuit(params[0], params[1])

plt.style.use("seaborn")
plt.bar(range(2**len(wires)), probs)
plt.show()
