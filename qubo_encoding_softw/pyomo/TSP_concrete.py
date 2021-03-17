from  pyomo.environ import * 
import numpy as np
import itertools as it

n = 4
w_concrete = np.arange(n**2).reshape((n, n))

# set up model

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
    for v in m.I:
        for w in m.I:
            if v != w:
                # probably there is a smarter way of doing it
                expr += w_matrix[v,w] * sum(m.x[t,v] * m.x[t+1,w] for t in m.Im1) 
                expr += w_matrix[v,w] * m.x[w_matrix.shape[0]-1,v] * m.x[1,w] 
    return expr

my_model.TimeConstraint = Constraint(my_model.I, rule=constraint_time)
my_model.CityConstraint = Constraint(my_model.I, rule=constraint_city)
my_model.OBJ = Objective(rule=lambda x:obj_expression(x, w_concrete))

