import pennylane as qml

t = 1
n = 2

dev = qml.device('default.qubit', wires=n)

def circ(theta):
    qml.RX(theta, wires=0)
    qml.Hadamard(wires=1)
    qml.CNOT(wires=[0,1])

# @qml.qnode(dev)
# def circuit(param):
#     circ(param)
#     return [qml.expval(qml.PauliZ(i)) for i in range(n)]
# 
# print("")
# circuit(0.5)
# print(circuit.draw())

# this is quantum circuit function
# it must return a measurement
@qml.qnode(dev)
def circuit(params, **kwargs):
    qml.layer(circ, 3, params)
    return [qml.expval(qml.PauliZ(i)) for i in range(n)]

print("")
circuit([0.3, 0.4, 0.5])
print(circuit.draw())
