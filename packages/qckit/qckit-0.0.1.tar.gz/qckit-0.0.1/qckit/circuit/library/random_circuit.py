"""Utility functions for generating random circuits."""

import numpy as np
import random

from qiskit.circuit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit import Reset
from qiskit.circuit.library.standard_gates import (
    IGate,
    U1Gate,
    U2Gate,
    U3Gate,
    XGate,
    YGate,
    ZGate,
    HGate,
    SGate,
    SXGate,
    SdgGate,
    TGate,
    TdgGate,
    RXGate,
    RYGate,
    RZGate,
    CXGate,
    CYGate,
    CZGate,
    CHGate,
    CRZGate,
    CU1Gate,
    CU3Gate,
    SwapGate,
    RZZGate,
    CCXGate,
    CSwapGate,
)
from qiskit.circuit.delay import Delay
from qiskit.circuit.exceptions import CircuitError

import copy

from .utils import check_seed, check_num_qubits

def random_circuit(backend,
    num_qubits, depth, max_operands=2, measure=False, conditional=False, reset=False, seed=None,
    qubits_list = None, identity = True, delay = False, delay_time = None, rz = True
):
    """Generate random circuit of arbitrary size and form.

    This function will generate a random circuit by randomly selecting gates
    from the set of standard gates in :mod:`qiskit.extensions`. For example:

    .. jupyter-execute::

        from qiskit.circuit.random import random_circuit

        circ = random_circuit(2, 2, measure=True)
        circ.draw(output='mpl')

    Args:
        backend: the backend where the native gates are selected
        num_qubits (int): number of quantum wires
        depth (int): layers of operations (i.e. critical path length)
        max_operands (int): maximum operands of each gate (between 1 and 3)
        measure (bool): if True, measure all qubits at the end
        conditional (bool): if True, insert middle measurements and conditionals
        reset (bool): if True, insert middle resets
        seed (int): sets random seed (optional)
        qubits_list(list or None): a list specified the indices of qubits to apply random gates.
            It must have the same length as `num_qubits`. Defaults to be `None`, and the qubits 
            are randomly selected
        delay(bool): if True, insert middle delays
        delay_time(list or None): the delay time is randomly chosen from the range [begin, end].
            If `None`, the range is [granularity, granularity * 100]. Note that the delay must
            be a multiple of the granularity of the backend

    Returns:
        QuantumCircuit: constructed circuit

    Raises:
        CircuitError: when invalid options given
    """
    if max_operands < 1 or max_operands > 3:
        raise CircuitError("max_operands must be between 1 and 3")

    random.seed(check_seed(seed))
    qubits_list = check_num_qubits(backend, num_qubits, qubits_list)

    b_num_qubits = backend.configuration().n_qubits
    qr = QuantumRegister(b_num_qubits, "q")
    qc = QuantumCircuit(b_num_qubits)

    backend_gates_list = backend.configuration().to_dict()["gates"]

    one_q_ops = []
    two_q_ops = []
    for backend_gate in backend_gates_list:
        gate_name = backend_gate["name"]
        if gate_name == "reset":
            continue
        for operands in backend_gate["coupling_map"]:
            flag = False
            for operand in operands:
                if operand not in qubits_list:
                    flag = True
                    break
            if flag:
                continue

            if gate_name == "id" and identity:
                one_q_ops.append([IGate, operands])
            elif gate_name == "rz" and rz:
                one_q_ops.append([RZGate, operands])
            elif gate_name == "sx":
                one_q_ops.append([SXGate, operands])
            elif gate_name == "x":
                one_q_ops.append([XGate, operands])
            elif gate_name == "cx":
                two_q_ops.append([CXGate, operands])
    
    one_param = [RZGate]
    two_param = []

    if delay:
        for operand in qubits_list:
            one_q_ops.append([Delay, [operand]])
        one_param.append(Delay)
        if not delay_time:
            granularity = backend.configuration().timing_constraints['granularity']
            delay_time = [granularity, granularity*100]
            delay_time_list = list(range(int(delay_time[0]/granularity)*granularity, int(delay_time[1]/granularity)*granularity + 1, granularity))

    if measure or conditional:
        cr = ClassicalRegister(b_num_qubits, "c")
        qc.add_register(cr)

    if reset:
        one_q_ops += [Reset]

    # apply arbitrary random operations at every depth
    for _ in range(depth):
        remaining_qubits = copy.deepcopy(qubits_list)
        random.shuffle(remaining_qubits)

        remaining_one_q_ops = copy.deepcopy(one_q_ops)
        remaining_two_q_ops = copy.deepcopy(two_q_ops)

        # choose either 1, 2, or 3 qubits for the operation
        while remaining_qubits:
            max_possible_operands = min(len(remaining_qubits), max_operands)
            if not remaining_two_q_ops:
                num_operands = 1
            else:
                num_operands = random.choice(range(max_possible_operands)) + 1
            # operands = [remaining_qubits.pop() for _ in range(num_operands)]
            if num_operands == 1:
                operation_operand = random.choice(remaining_one_q_ops)
            elif num_operands == 2:
                operation_operand = random.choice(remaining_two_q_ops)
            # elif num_operands == 3:
            #     operation_operand = random.choice(three_q_ops)

            operation = operation_operand[0]
            operands = operation_operand[1]

            for operand in operands:
                remaining_qubits.remove(operand)

            if operation in one_param:
                num_params = 1
            elif operation in two_param:
                num_params = 2
            # elif operation in three_param:
            #     num_angles = 3
            else:
                num_params = 0

            if issubclass(operation, Delay):
                params = [int(random.choice(delay_time_list))]
            else:
                params = [random.uniform(0, 2 * np.pi) for x in range(num_params)]
            register_operands = [qr[i] for i in operands]
            op = operation(*params)

            # with some low probability, condition on classical bit values
            # if conditional and random.choice(range(10)) == 0:
            #     value = random.integers(0, np.power(2, b_num_qubits))
            #     op.condition = (cr, value)

            qc.append(op, register_operands)

            # update the gate set
            remaining_one_q_ops_after = []
            remaining_two_q_ops_after = []
            for i in range(len(remaining_one_q_ops)):
                flag = True
                for operand in remaining_one_q_ops[i][1]:
                    if operand not in remaining_qubits:
                        flag = False
                        break
                if flag:
                    remaining_one_q_ops_after.append(remaining_one_q_ops[i])
            for i in range(len(remaining_two_q_ops)):
                flag = True
                for operand in remaining_two_q_ops[i][1]:
                    if operand not in remaining_qubits:
                        flag = False
                        break
                if flag:
                    remaining_two_q_ops_after.append(remaining_two_q_ops[i])
            remaining_one_q_ops = remaining_one_q_ops_after
            remaining_two_q_ops = remaining_two_q_ops_after

    if measure:
        qc.measure(qr, cr)

    return qc



if __name__ == "__main__":
    from qiskit import IBMQ
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub="ibm-q", group="open", project="main")

    backend = provider.get_backend("ibmq_lima")
    num_qubits = 3
    qubits_list = [1, 3, 4]
    depth = 6 # 10
    seed = 11

    qc = random_circuit(backend, num_qubits, depth, seed=seed, qubits_list=qubits_list, delay=False) # delay=True
    print(qc.draw("text"))
