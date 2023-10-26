from .random_circuit import random_circuit
from .deutsch_jozsa import deutsch_jozsa
from .bernstein_vazirani import bernstein_vazirani
from .fourier import fourier
from .grover import grover

if __name__ == "__main__":
    from qiskit import IBMQ
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub="ibm-q", group="open", project="main")


    backend = provider.get_backend("ibmq_lima")
    num_qubits = 3
    qubits_list = [1, 3, 4]


    print("random_circuit\n")

    depth = 3
    seed = 11
    
    qc = random_circuit(backend, num_qubits, depth, seed=seed, qubits_list=qubits_list, delay=False) # delay=True
    print(qc.draw("text"))





    print("\n\n\ndeutsch_jozsa\n")

    function_type = "balanced"
    b_str = "10"
    measure = False

    qc = deutsch_jozsa(backend, num_qubits, qubits_list = qubits_list, function_type = function_type, b_str = b_str, measure = measure) # delay=True
    print(qc.draw("text"))





    print("\n\n\nbernstein_vazirani\n")

    hidden_str = "10"
    measure = False

    qc = bernstein_vazirani(backend, num_qubits, qubits_list = qubits_list, hidden_str = hidden_str, measure = measure) # delay=True
    print(qc.draw("text"))




    print("\n\n\nfourier\n")

    approximation_degree = 0
    do_swaps = True
    inverse = False
    measure = False

    qc = fourier(backend, num_qubits, qubits_list = qubits_list, approximation_degree = approximation_degree, do_swaps = do_swaps, inverse = inverse, measure = measure) # delay=True
    print(qc.draw("text"))




    print("\n\n\ngrover\n")

    iterations = 1
    search_state = "000"
    measure = False

    qc = grover(backend, num_qubits, qubits_list = qubits_list, iterations = iterations, search_state = search_state, measure = measure) # delay=True
    print(qc.draw("text"))
    