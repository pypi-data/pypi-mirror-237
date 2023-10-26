from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import GroverOperator
from qiskit.quantum_info import Statevector



def grover(num_qubits, qubits_list = None, iterations = 1, search_state = None, measure = True):
    if not search_state:
        search_state = "0" * num_qubits
    elif len(search_state) != num_qubits:
        raise ValueError("Search state length is different from qubits in qubit_layout")

    mark_state = Statevector.from_label(search_state)
    
    # specify the Grover operator
    grover_op = GroverOperator(mark_state, insert_barriers=True).decompose()

    # create the Grover's search circuit
    qc = QuantumCircuit(num_qubits, num_qubits)
    # initialize the states
    qc.h(qubits_list)
    # apply the Grover operator `iterations` times
    for _ in range(iterations):
        qc.append(grover_op.decompose(), qubits_list)
    qc = qc.decompose()
    
    # measure the results
    if measure:
        qc.measure(qubits_list, range(num_qubits))
    
    return qc



if __name__ == "__main__":
    num_qubits = 3
    qubits_list = [1, 3, 4]
    iterations = 1
    search_state = "000"
    measure = False

    qc = grover(num_qubits, qubits_list = qubits_list, iterations = iterations, search_state = search_state, measure = measure)
    print(qc.draw("text"))
