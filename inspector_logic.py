import dimod
import dwave.inspector

from dwave.system import DWaveSampler, EmbeddingComposite


bqm = dimod.BQM.from_ising({}, {'ab': 1, 'bc': 1, 'ca': 1})
sampler = EmbeddingComposite(DWaveSampler(solver=dict(qpu=False)))