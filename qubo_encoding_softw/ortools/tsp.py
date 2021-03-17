from ortools.sat.python import cp_model
import numpy as np
import itertools as it

model = cp_model.CpModel()


city_no = 4
w_matrix = np.random.rand(city_no, city_no)
w_matrix += np.transpose(w_matrix)

my_var = {}
for t in range(city_no):
    for v in range(city_no):
        my_var[(t, v)] = model.NewBoolVar('var_t%iv%i' % (t, v))

for t in range(city_no):
    model.Add(sum(my_var[(t,v)] for v in range(city_no)) == 1) 

for v in range(city_no):
    model.Add(sum(my_var[(t,v)] for t in range(city_no)) == 1) 

for t in range(city_no):
    model.Add(sum(my_var[(t,v)] for v in range(city_no)) == 1) 

model.Add(my_var[(0,0)] + my_var[(0,1)] == 1)
# print(my_var[(0,0)] * my_var[(0,1)])
model.AddMinEquality(sum(w_matrix[v,w]*my_var[(t,v)]*my_var[((t+1)%n,v)] if v !=w else 0 for t,v,w in it.product(range(city_no), repeat=3)))
print(model)