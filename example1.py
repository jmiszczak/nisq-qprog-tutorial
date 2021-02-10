import pennylane as qml

H = qml.Hamiltonian(
        [1, 1, 0.5],
        [qml.PauliX(0), qml.PauliZ(1), qml.PauliX(0) @ qml.PauliX(1)]
        )

print (H)


t = 1
n = 2

dev = qml.device('default.qubit', wires=n)

@qml.qnode(dev)
def circuit():
    qml.templates.ApproxTimeEvolution(H, t, n)
    return [qml.expval(qml.PauliZ(i)) for i in range(n)]

circuit()
print(circuit.draw())
