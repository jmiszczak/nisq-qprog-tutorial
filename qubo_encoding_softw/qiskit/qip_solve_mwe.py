from qiskit.optimization import QuadraticProgram
from docplex.mp.model import Model
from dwave.plugins.qiskit import DWaveMinimumEigensolver
from qiskit.optimization.algorithms import MinimumEigenOptimizer

# Create docplex model
mdl = Model("QIP")
x = mdl.integer_var(name='x', lb=0, ub=4)
y = mdl.integer_var(name='y', lb=0, ub=3)
mdl.minimize(x + y**2)
mdl.add_constraint(x + y <= 2)

# convert to qiskit's QuadraticProgram
mod = QuadraticProgram()
mod.from_docplex(mdl)

# solve
dwave_mes = DWaveMinimumEigensolver()
optimizer = MinimumEigenOptimizer(dwave_mes)
optimizer.solve(mod)


