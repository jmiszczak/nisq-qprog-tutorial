from  pyomo.environ import * 
import numpy as np
import itertools as it

n = 4
w_concrete = np.arange(n**2).reshape((n, n))

my_model = ConcreteModel()
my_model.I = RangeSet(0, n-1)
my_model.Im1 = RangeSet(0, n-2)
my_model.x = Var(my_model.I, my_model.I, domain=Binary)

def constraint_time(m, t):
    return sum(m.x[t,i] for i in m.I) == 1 
def constraint_city(m, v):
    return sum(m.x[i,v] for i in m.I) == 1 

def obj_expression(m, w_matrix):
    expr = 0.
    for v, w in it.product(m.I, repeat=2):
        if v != w:
            expr += w_matrix[v,w] * sum(m.x[t,v] * m.x[t+1,w] for t in m.Im1) 
            expr += w_matrix[v,w] * m.x[w_matrix.shape[0]-1,v] * m.x[1,w] 
    return expr

my_model.TC = Constraint(my_model.I, rule=constraint_time)
my_model.CC = Constraint(my_model.I, rule=constraint_city)
my_model.OBJ = Objective(rule=lambda x:obj_expression(x, w_concrete))

opt = SolverFactory('cplex')
results = opt.solve(my_model)

print("Objective value", value(my_model.OBJ))
print("Solution")
for i,j in it.product(range(n), repeat=2):
    print("x[{},{}] =".format(i,j), value(my_model.x[i,j]))