from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT



def fourier(num_qubits, qubits_list = None, approximation_degree=0, do_swaps=True, inverse=False, measure = True):
    qc = QuantumCircuit(num_qubits, num_qubits)
    qft = QFT(num_qubits, approximation_degree=approximation_degree, do_swaps=do_swaps, inverse=inverse).decompose()
    qc.append(qft, qubits_list)
    qc = qc.decompose()

    # measure the results
    if measure:
        qc.measure(qubits_list, range(num_qubits))
    
    return qc



if __name__ == "__main__":
    num_qubits = 3
    qubits_list = [1, 3, 4]
    approximation_degree = 0
    do_swaps = True
    inverse = False
    measure = False

    qc = fourier(num_qubits, qubits_list = qubits_list, approximation_degree = approximation_degree, do_swaps = do_swaps, inverse = inverse, measure = measure)
    print(qc.draw("text"))
