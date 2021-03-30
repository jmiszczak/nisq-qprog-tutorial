from qiskit.optimization import QuadraticProgram
from qiskit.optimization.converters.quadratic_program_to_qubo import QuadraticProgramToQubo
from docplex.mp import model_reader
from dwave.plugins.qiskit import DWaveMinimumEigensolver


docplex_mod = model_reader.ModelReader.read("trial.lp")
mod = QuadraticProgram()
mod.from_docplex(docplex_mod)
conv = QuadraticProgramToQubo()

print(mod)

mod_qubo = conv.convert(mod)
print(mod_qubo)
operator, offset = mod_qubo.to_ising()
bqm = DWaveMinimumEigensolver()._operator_to_bqm(operator)
print(bqm)