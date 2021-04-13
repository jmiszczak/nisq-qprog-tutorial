from  pyomo.environ import * 
import numpy as np
import itertools as it

n = 4
w_concrete = np.arange(n**2).reshape((4,4))
print(w_concrete)

## QCBO Abstract model TSP QUBO

## QCBO Abstract model TSP QUBO

my_model = AbstractModel()

my_model.city_no = Param(within=PositiveIntegers)
my_model.I = RangeSet(1, my_model.city_no)
my_model.Im1 = RangeSet(1, my_model.city_no - 1)


my_model.W = Param(my_model.I, my_model.I, initialize=1)
my_model.x = Var(my_model.I, my_model.I, domain=Binary)

def constraint_time(m, t):
    return sum(m.x[t,i] for i in m.I) == 1 

def constraint_city(m, v):
    return sum(m.x[i,v] for i in m.I) == 1 

def obj_expression(m):
    expr = 0.
    for v in m.I:
        for w in m.I:
            if v != w:
                expr += m.W[v,w] * sum(m.x[t,v] * m.x[t+1,w] for t in m.Im1) 
                expr += m.W[v,w] * m.x[m.city_no,v] * m.x[1,w] 
    return expr

my_model.OBJ = Objective(rule=obj_expression)
my_model.TimeConstraint = Constraint(my_model.I, rule=constraint_time)
my_model.CityConstraint = Constraint(my_model.I, rule=constraint_city)

print("###################################################")
data = {None: {
    'city_no': {None: n},
    'W': { (i+1,j+1): w_concrete[i,j] for i,j in it.product(range(n), repeat=2)}
}}

instance = my_model.create_instance(data)
print(instance.is_constructed())

opt = SolverFactory('cplex')
results = opt.solve(instance)

print("Objective value")
print(value(instance.OBJ))
print("Solution")
for i, j in it.product(range(1,n+1), repeat=2):
    print("x[{},{}] =".format(i,j), value(instance.x[i,j]))

print("Constraint test")
for i in instance.I:
    print(value(instance.TimeConstraint[i]))
    print(value(instance.CityConstraint[i]))


## QUBO
