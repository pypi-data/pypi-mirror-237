from qiskit.circuit import QuantumCircuit



def bernstein_vazirani(num_qubits, qubits_list = None, hidden_str = None, measure = True):
    if num_qubits < 2:
        raise ValueError("Bernstein-Vazirani algorithms must have at least 2 qubits!")

    if not hidden_str:
        hidden_str = "0" * (num_qubits - 1)

    if len(hidden_str) != num_qubits - 1:
        raise ValueError("The length of the hidden_str is not equal to num_qubits - 1")

    qc = QuantumCircuit(num_qubits, num_qubits - 1)
    qc.h(qubits_list)
    qc.z(qubits_list[-1])

    # Apply the inner-product oracle
    hidden_str = hidden_str[::-1] # reverse s to fit qiskit's qubit ordering
    for i in range(num_qubits - 1):
        if hidden_str[i] == '0':
            qc.i(qubits_list[i])
        else:
            qc.cx(qubits_list[i], qubits_list[-1])

    qc.h(qubits_list[:-1])

    # measure the results
    if measure:
        qc.measure(qubits_list[:-1], range(num_qubits - 1))
    
    return qc



if __name__ == "__main__":
    num_qubits = 3
    qubits_list = [1, 3, 4]
    hidden_str = "10"
    measure = False

    qc = bernstein_vazirani(num_qubits, qubits_list = qubits_list, hidden_str = hidden_str, measure = measure)
    print(qc.draw("text"))
