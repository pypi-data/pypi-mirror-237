from qiskit.circuit import QuantumCircuit, Gate
from qiskit.circuit.library.standard_gates.x import XGate

def state_prep_circ(state_begin, state_end, num_qubits, qubit_list=None, sched=None):
    """
    Generates a quantum circuit to prepare a specific quantum state.

    Args:
        state_begin (int): Starting state index (inclusive).
        state_end (int): Ending state index (exclusive).
        num_qubits (int): Number of qubits in the circuit.
        qubit_list (list, optional): List of qubits to apply the state preparation gates. Defaults to None.
        sched (Sched, optional): Scheduler object for obtaining gate schedules. Defaults to None.

    Returns:
        QuantumCircuit: Quantum circuit for state preparation.
    """
    if sched and num_qubits > sched.num_qubits:
        raise Exception("The number of qubits in `qubit_list` is larger than the number of qubits the backend has!")

    circ = QuantumCircuit(num_qubits)

    state_range = range(state_begin, state_end) if state_begin <= state_end else range(state_begin - 1, state_end - 1, -1)

    pi_gate_list = [XGate() if i == 0 else Gate(f"pi_{i}_{i + 1}", 1, []) for i in state_range]
    for qubit in qubit_list:
        for i, curr_state in enumerate(state_range):
            if curr_state == 0:
                circ.x(qubit)
            else:
                circ.append(pi_gate_list[i], [qubit])
                circ.add_calibration(pi_gate_list[i], (qubit,), sched.get_sched(label=f"pi_{curr_state}_{curr_state + 1}", qubit=qubit))

    return circ


def one_level_reset(reset_level, num_qubits, qubit_list=None, sched=None):
    """
    Generates a quantum circuit to perform a single level of qubit reset.

    Args:
        reset_level (int): Reset level (number of times to reset the qubits).
        num_qubits (int): Number of qubits in the circuit.
        qubit_list (list, optional): List of qubits to reset. Defaults to None.
        sched (Sched, optional): Scheduler object for obtaining gate schedules. Defaults to None.

    Returns:
        QuantumCircuit: Quantum circuit for one level of qubit reset.
    """
    circ = state_prep_circ(state_begin=reset_level, state_end=1, num_qubits=num_qubits, qubit_list=qubit_list, sched=sched)
    circ.reset(qubit_list)

    return circ


def secure_reset(reset_level, num_qubits, qubit_list=None, sched=None):
    """
    Generates a quantum circuit to perform secure reset on qubits.

    Args:
        reset_level (int): Reset level (number of times to reset the qubits).
        num_qubits (int): Number of qubits in the circuit.
        qubit_list (list, optional): List of qubits to reset. Defaults to None.
        sched (Sched, optional): Scheduler object for obtaining gate schedules. Defaults to None.

    Returns:
        QuantumCircuit: Quantum circuit for secure qubit reset.
    """
    circ = QuantumCircuit(num_qubits)
    for curr_reset_level in range(1, reset_level + 1):
        circ = circ.compose(one_level_reset(reset_level=curr_reset_level, num_qubits=num_qubits, qubit_list=qubit_list, sched=sched))
    return circ


if __name__ == "__main__":
    from qiskit import schedule
    from sched import Sched
    from qcutils.credential import load_provider

    provider = load_provider()
    backend = provider.get_backend("ibm_lagos")
    sched = Sched(backend)
    sched.load_gate_data()
    circ = state_prep_circ(state_begin=0, state_end=3, num_qubits=backend.configuration().n_qubits, qubit_list=[1, 3, 5], sched=sched)
    print(circ.draw("text"))
    # print(schedule(circ, backend).instructions)
