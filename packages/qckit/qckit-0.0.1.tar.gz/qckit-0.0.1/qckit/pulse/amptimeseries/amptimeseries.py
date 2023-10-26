import numpy as np
from ..channel import channel_rep
from qiskit import transpile, schedule
from qiskit.pulse import Play
from qiskit.pulse.library.symbolic_pulses import SymbolicPulse
from qiskit.pulse.library.waveform import Waveform


def add_time_series(a, b):
    """
    Adds two one-dimensional numpy arrays element-wise and returns the result.

    Args:
        a (numpy.ndarray): First input array.
        b (numpy.ndarray): Second input array.

    Returns:
        numpy.ndarray: Element-wise sum of input arrays.
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    elif len(a.shape) > 1 or len(b.shape) > 1:
        raise ValueError("Inputs must be one dimension!")
    elif a.shape[0] < b.shape[0]:
        return np.concatenate((a, np.zeros(b.shape[0] - a.shape[0]))) + b
    else:
        return a + np.concatenate((b, np.zeros(a.shape[0] - b.shape[0])))



def square_real_imag(amp_time_series_dict):
    """
    Computes the square of the norm of complex numbers in the input dictionary.

    Args:
        amp_time_series_dict (Dict[str, numpy.ndarray]): Dictionary of amplitude time series.

    Returns:
        numpy.ndarray: Square of the norm of complex numbers for each time step.
    """
    return np.square(np.linalg.norm(list(amp_time_series_dict.values()), axis=0))

def total_amp_time_series(amp_time_series_dict, func=None):
    """
    Computes the total amplitude time series using the specified function.

    Args:
        amp_time_series_dict (Dict[str, numpy.ndarray]): Dictionary of amplitude time series.
        func (callable): Function to apply to the amplitude time series (default is square_real_imag).

    Returns:
        numpy.ndarray: Total amplitude time series.
    """
    if not func:
        func = square_real_imag
    return func(amp_time_series_dict)



def sched_to_amp_time_series(sched, scale=1, total=False, func=None, use_channel=False):
    """
    Converts a Qiskit pulse Schedule object to amplitude time series.

    Args:
        sched (Schedule): Qiskit pulse Schedule object.
        scale (float): Scaling factor for the amplitude time series (default is 1).
        total (bool): If True, compute total amplitude time series (default is False).
        func (callable): Function to apply for computing total amplitude time series.
        use_channel (bool): If True, use channel names as `Channel` objects; otherwise, use strings.

    Returns:
        Dict[str, numpy.ndarray]: Dictionary of amplitude time series for each channel.
    """
    duration = sched.duration
    amp_time_series_dict = {}
    
    for channel in sched.channels:
        channel = channel_rep(channel, use_channel=use_channel)
        amp_time_series_dict[channel] = np.zeros(duration, dtype="complex")

    for time_step, operation in sched.instructions:
        if isinstance(operation, Play):
            channel = channel_rep(operation.channel, use_channel=use_channel)
            if isinstance(operation.pulse, SymbolicPulse):
                amp_time_series_dict[channel][time_step:time_step+operation.duration] = operation.pulse.get_waveform().samples * scale
            elif isinstance(operation.pulse, Waveform):
                amp_time_series_dict[channel][time_step:time_step+operation.duration] = operation.pulse.samples * scale
            else:
                raise ValueError("Pulse object is incorrect!")
    
    if total:
        if not func:
            func = square_real_imag
        amp_time_series_dict = total_amp_time_series(amp_time_series_dict, func = func)

    return amp_time_series_dict

def circ_to_amp_time_series(circ, backend, scale=1, total=False, func=None, use_channel=True, do_transpile=True, **transpiler_args):
    """
    Converts a QuantumCircuit object to amplitude time series.

    Args:
        circ (QuantumCircuit): Input quantum circuit.
        backend (Backend): Backend object for transpilation and scheduling.
        scale (float): Scaling factor for the amplitude time series (default is 1).
        total (bool): If True, compute total amplitude time series (default is False).
        func (callable): Function to apply for computing total amplitude time series.
        use_channel (bool): If True, use channel names as `Channel` objects; otherwise, use strings.
        do_transpile (bool): If True, transpile the circuit using specified transpiler arguments.

    Returns:
        Dict[str, numpy.ndarray]: Dictionary of amplitude time series for each channel.
    """
    if do_transpile:
        circ = transpile(circ, backend, **transpiler_args)
    
    sched = schedule(circ, backend)
    
    if not func:
        func = square_real_imag
    
    return sched_to_amp_time_series(sched, scale=scale, total=total, func=func, use_channel=use_channel)
