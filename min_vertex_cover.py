import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pennylane as qml
import pennylane.qaoa as qaoa

edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
graph = nx.Graph(edges)

#nx.draw(graph, with_labels=True)
#plt.show()

cost_h, mixer_h = qaoa.min_vertex_cover(graph, constrained=False)
print ('Cost Hamiltonian', cost_h)
print ('Mixer Hamiltonian', mixer_h)

def qaoa_layer(gamme, alpha):
    qaoa.cost_layer(gamma, cost_h)
    qaoa.mixer_layer(alpha, mixer_h)

wires = range(4)
depth = 2

def circuit(params, **kwargs):
    for w in wires:
        qml.Hadamaed(widers=w)
    qml.layer(qaoa_layer, depth, params[0], params[1])

dev = qml.device("qulacs.simulator", wires=wires)
cost_function = qml.ExpvalCost(circuit, cost_h, dev)

optimzer = qml.GradientDescentOptimizer()
steps = 70
params = [[0.5, 0.5], [0.5, 0.5]]
