from qiskit.optimization import QuadraticProgram
from qiskit.optimization.converters.quadratic_program_to_qubo import QuadraticProgramToQubo
from docplex.mp.model import Model
from dwave.plugins.qiskit import DWaveMinimumEigensolver

# Create docplex model
mdl = Model("QIP")
x = mdl.integer_var(name='x', lb=0, ub=4)
y = mdl.integer_var(name='y', lb=0, ub=3)
# the following gives error on docplex
# mdl.minimize((x + y)**3) 
mdl.minimize(x + y**2)
mdl.add_constraint(x + y <= 2)

# the following gives error on qiskit
# mdl.add_constraint(x + y**2 <= 2) 

# convert to qiskit's QuadraticProgram
mod = QuadraticProgram()
mod.from_docplex(mdl)
print(mod)

# convert to QUBO
conv = QuadraticProgramToQubo()
mod_qubo = conv.convert(mod)
print(mod_qubo)

# convert to bqm
operator, offset = mod_qubo.to_ising()
bqm = DWaveMinimumEigensolver()._operator_to_bqm(operator)
print(bqm)

