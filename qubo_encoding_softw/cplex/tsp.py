from docplex.mp.model import Model
import docplex.mp.solution as Solucion
import numpy as np
print(Solucion)

n=11
ciudades=[i for i in range(n)] # Creamos ciudades de la 0 a la 9  
arcos =[(i,j) for i in ciudades for j in ciudades if i!=j]

random=np.random
random.seed(1)
coord_x=random.rand(n)*100
coord_y=random.rand(n)*100

distancia={(i, j): np.hypot(coord_x[i] - coord_x[j], coord_y[i] - coord_y[j]) for i,j in arcos}


mdl=Model('TSP')
x=mdl.binary_var_dict(arcos,name='x')
d=mdl.continuous_var_dict(ciudades,name='d')
print(list(filter(lambda el: el.count("var_dict") > 0 , dir(mdl))))
mdl.minimize(mdl.sum(distancia[i]*x[i] for i in arcos))

for c in ciudades:
    mdl.add_constraint(mdl.sum(x[(i,j)] for i,j in arcos if i==c)==1, 
                       ctname='out_%d'%c)
for c in ciudades:
    mdl.add_constraint(mdl.sum(x[(i,j)] for i,j in arcos if j==c)==1, 
                       ctname='in_%d'%c)

for i,j in arcos:
    if j!=0:
        mdl.add_indicator(x[(i,j)],d[i]+1==d[j], 
                          name='order_(%d,_%d)'%(i, j))


mdl.parameters.timelimit=120
mdl.parameters.mip.strategy.branch=1
mdl.parameters.mip.tolerances.mipgap=0.15

solucion = mdl.solve(log_output=True)

