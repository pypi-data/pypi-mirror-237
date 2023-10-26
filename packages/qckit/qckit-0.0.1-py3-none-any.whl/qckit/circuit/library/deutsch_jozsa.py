from qiskit.circuit import QuantumCircuit



def deutsch_jozsa(num_qubits, qubits_list = None, function_type = "constant", b_str = None, measure = True):
    if function_type not in ["constant", "balanced"]:
        raise ValueError("function_type must be either \"contant\" or \"balanced\"!")

    if num_qubits < 2:
        raise ValueError("Deutsch-Jozsa algorithms must have at least 2 qubits!")

    if not b_str:
        b_str = "0" * (num_qubits - 1)

    if len(b_str) != num_qubits - 1:
        raise ValueError("The length of the b_str is not equal to num_qubits - 1")

    qc = QuantumCircuit(num_qubits, num_qubits - 1)
    qc.x(qubits_list[-1])
    qc.h(qubits_list)

    if function_type == "balanced":
        for i in range(num_qubits - 1):
            if b_str[i] == '1':
                qc.x(qubits_list[i])
            qc.cx(qubits_list[i], qubits_list[-1])
            if b_str[i] == '1':
                qc.x(qubits_list[i])

    qc.h(qubits_list[:-1])

    # measure the results
    if measure:
        qc.measure(qubits_list[:-1], range(num_qubits - 1))
    
    return qc



if __name__ == "__main__":
    num_qubits = 3
    qubits_list = [1, 3, 4]
    function_type = "balanced"
    b_str = "10"
    measure = False

    qc = deutsch_jozsa(num_qubits, qubits_list = qubits_list, function_type = function_type, b_str = b_str, measure = measure)
    print(qc.draw("text"))
