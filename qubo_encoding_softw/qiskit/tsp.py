from qiskit.optimization.applications.ising import tsp
from qiskit.optimization.applications.ising.common import sample_most_likely
from dwave.plugins.qiskit import DWaveMinimumEigensolver

six_cities_tsp = tsp.random_tsp(6, seed=123)
operator, offset = tsp.get_operator(six_cities_tsp)
print(operator.print_details())
print(operator.num_qubits)

bqm = DWaveMinimumEigensolver()._operator_to_bqm(operator)
print(bqm)