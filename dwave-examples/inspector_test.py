from dwave.system import DWaveSampler
import dwave.inspector


#sampler = DWaveSampler(client="base")
sampler = DWaveSampler(solver=dict(qpu=True))
h = {}

J = {(0, 4): 1, (0, 5): 1, (1, 4): 1, (1, 5): -1}

all(edge in sampler.edgelist for edge in J)

# Sample

response = sampler.sample_ising(h, J, num_reads=100)


# Inspect

dwave.inspector.show(response)  
