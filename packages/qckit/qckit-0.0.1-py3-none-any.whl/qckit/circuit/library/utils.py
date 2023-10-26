import random
import numpy as np

def check_seed(seed):
    if seed is None:
        seed = random.randint(0, np.iinfo(np.int32).max)
    return seed

def check_num_qubits(backend, num_qubits, qubits_list):
    b_num_qubits = backend.configuration().n_qubits

    if qubits_list:
        if len(qubits_list) != num_qubits:
            raise Exception("num_qubits is not equal to the length of qubits_list!")
        for qubit in qubits_list:
            if qubit >= b_num_qubits:
                raise Exception("Qubit indices are out of range!")
    else:
        if num_qubits > b_num_qubits:
            raise Exception("The backend does not have enough qubits as!")
        else:
            qubits_list = random.sample(range(b_num_qubits), num_qubits)
    
    return qubits_list

