import random, itertools, multiprocessing, functools
from qiskit import transpile, schedule

def expand_by_layout(benchmark, backend, circ_idx_list = None, num_layout = 1, seed_layout = 0, **transpiler_args):
    """
    Expands a list of circuits by transpiling them to a specified backend with different initial layouts.

    Args:
        benchmark (Benchmark): A benchmark object containing the circuits to be expanded.
        backend (BaseBackend): The backend to transpile the circuits to.
        circ_idx_list (list[int]): A list of indices of the circuits to be expanded. If None, all circuits in the benchmark
            will be expanded.
        num_layout (int): The number of different initial layouts to use for each circuit.
        seed_layout (int): The seed for the random number generator used to select the initial layouts.
        **transpiler_args: Additional arguments to be passed to the transpiler.

    Returns:
        list: A list of schedules obtained by transpiling the input circuits with different initial layouts.
    """

    # Set the seed for the random number generator
    random.seed(seed_layout)

    # Get the number of qubits in the backend
    b_num_qubits = backend.configuration().n_qubits

    # If no circuit indices are specified, expand all circuits in the benchmark
    if not circ_idx_list:
        circ_idx_list = list(range(len(benchmark)))

    # Create a list of circuit names for error reporting
    circ_name_list = []
    for circ_idx in circ_idx_list:
        circ_name_list.append(benchmark.circ_name_list[circ_idx])

    # Create a list of schedules obtained by transpiling the input circuits with different initial layouts
    schedule_list = []
    for i, circ in enumerate(benchmark[circ_idx_list]):
        num_qubits = circ.num_qubits

        # Attempt to schedule the circuit, and skip it if it cannot be scheduled
        try:
            schedule(transpile(circ, backend), backend)
        except:
            print(f"Circuit {circ_name_list[i]} is removed since it cannot be schedule!")
            continue

        # Generate a list of all possible initial layouts for the circuit
        layout_list = list(itertools.permutations(range(b_num_qubits), num_qubits))

        # Choose a random subset of initial layouts from the list
        k = min(len(layout_list), num_layout)
        selected_layout = []
        while len(selected_layout) < k:
            item = random.choice(layout_list)
            if item not in selected_layout:
                selected_layout.append(list(item))

        # Transpile the circuit with each initial layout and add the resulting schedule to the list
        for initial_layout in selected_layout:
            transpiled_circ = transpile(circ, backend, initial_layout=initial_layout, **transpiler_args)
            schedule_list.append(schedule(transpiled_circ, backend))

    return schedule_list


def multi_process(func, args, num_process = 1):
    """
    Runs a function in parallel using multiple processes.

    Args:
        func (function): The function to run in parallel.
        args (tuple): A tuple of arguments to pass to the function.
        num_process (int): The number of processes to use.

    Returns:
        list: A list of results obtained by running the function in parallel.
    """
    # Split the benchmark into chunks for each process
    benchmark = args[0]
    total_len = len(benchmark)
    process_len = int(total_len/num_process)
    process_len = process_len + 1 if total_len % num_process else process_len

    # Create a pool of processes and run the function on each chunk of the benchmark
    pool = multiprocessing.Pool(num_process)
    results = pool.starmap(func, zip([benchmark[p_idx * process_len: p_idx * (process_len+1)] for p_idx in range(num_process)], itertools.repeat(args[1:])))
    result = functools.reduce(lambda a, b: a + b, results)

    return result
