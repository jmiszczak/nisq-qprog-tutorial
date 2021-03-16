# based on example based on from https://github.com/recruit-communications/pyqubo/blob/master/notebooks/TSP.ipynb
from pyqubo import Array, Placeholder, Constraint
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from time import time 

# Prepare binary vector with  bit $(i, j)$ representing to visit $j$ city at time $i$ 

n_city = 60
d = np.random.rand(n_city, n_city)
d += np.transpose(d)
x = Array.create('c', (n_city, n_city), 'BINARY')

# Constraint not to visit more than two cities at the same time.
time_const = 0.0
for i in range(n_city):
    # If you wrap the hamiltonian by Const(...), this part is recognized as constraint
    time_const += Constraint((sum(x[i, j] for j in range(n_city)) - 1)**2, label="time{}".format(i))

# Constraint not to visit the same city more than twice.
city_const = 0.0
for j in range(n_city):
    city_const += Constraint((sum(x[i, j] for i in range(n_city)) - 1)**2, label="city{}".format(j))

# distance of route
distance = 0.0
for i in range(n_city):
    for j in range(n_city):
        for k in range(n_city):
            distance += d[i,j] * x[k, i] * x[(k+1)%n_city, j]

# Construct hamiltonian
A = Placeholder("A")
H = distance + A * (time_const + city_const)

# Compile model
model = H.compile()

# Generate QUBO
feed_dict = {'A': 4.0}
t1 = time()
bqm = model.to_bqm(feed_dict=feed_dict)
print("to bqm", time() - t1)

t1 = time()
bqm = model.to_ising(feed_dict=feed_dict)
print("to ising", time() - t1)

# import neal
# sa = neal.SimulatedAnnealingSampler()
# sampleset = sa.sample(bqm, num_reads=100, num_sweeps=100)

# # Decode solution
# decoded_samples = model.decode_sampleset(sampleset, feed_dict=feed_dict)
# best_sample = min(decoded_samples, key=lambda x: x.energy)
# num_broken = len(best_sample.constraints(only_broken=True))
# print("number of broken constarint = {}".format(num_broken))
