from pyqubo import Array, UnaryEncInteger, LogEncInteger, Constraint, Placeholder
import neal

a = LogEncInteger("a", (0, 5))
b = LogEncInteger("b", (0, 6))
c = LogEncInteger("c", (0, 4))

H = -a*b*c
print(H)
print(dir(H))

model = H.compile()
bqm = model.to_bqm()

sa = neal.SimulatedAnnealingSampler()
sampleset = sa.sample(bqm, num_reads=100, num_sweeps=100)

# Decode solution
decoded_samples = model.decode_sampleset(sampleset)
best_sample = min(decoded_samples, key=lambda x: x.energy)
num_broken = len(best_sample.constraints(only_broken=True))
print("number of broken constarint = {}".format(num_broken))
print("a =", best_sample.subh['a'])
print("b =", best_sample.subh['b'])
print("c =", best_sample.subh['c'])
