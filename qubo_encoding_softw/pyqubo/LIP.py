from pyqubo import Array, UnaryEncInteger, LogEncInteger, Constraint, Placeholder

city_no = 4

# obj: 2*a+3*b
# constr: 4*a - 3*b == 2
# constr: 2*a + b <= 10

a = UnaryEncInteger("a", (0, 10))
b = LogEncInteger("b", (0, 12))
s1 = LogEncInteger("s1", (0, 7))

objective = 2*a+3*b
print(objective)

A = Placeholder("A")
B = Placeholder("B")
constraint1 = Constraint((4*a - 3*b - 2)**2, label="con1")
constraint2 = Constraint((2*a + b - 10 + s1 )**2, label="con2")

H = objective + A*constraint1 + B*constraint2
model = H.compile()
feed_dict = {'A': 10., 'B': 10} # guessed
bqm = model.to_bqm(feed_dict=feed_dict)


import neal
sa = neal.SimulatedAnnealingSampler()
sampleset = sa.sample(bqm, num_reads=100, num_sweeps=100)

# Decode solution
decoded_samples = model.decode_sampleset(sampleset, feed_dict=feed_dict)
best_sample = min(decoded_samples, key=lambda x: x.energy)
num_broken = len(best_sample.constraints(only_broken=True))
print("number of broken constarint = {}".format(num_broken))
print(best_sample)
print(best_sample.subh['a'])
print(best_sample.subh['b'])
print(best_sample.subh['s1'])
