from dwave.system import DWaveSampler
import dwave.inspector
import dwave

# Get solver
sampler = DWaveSampler(solver=dict(qpu=True))

# Define a problem (actual qubits depend on the selected QPU's working graph)
h = {}
J = {(0, 4): 1, (0, 5): 1, (1, 4): 1, (1, 5): -3}
assert all(edge in sampler.edgelist for edge in J)

# Sample
response = sampler.sample_ising(h, J, num_reads=100)

# Inspect
dwave.inspector.show(response)