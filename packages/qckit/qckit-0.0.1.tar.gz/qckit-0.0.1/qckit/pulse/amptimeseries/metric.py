import numpy as np
from qiskit import QuantumCircuit
from .circamptimeseries import CircAmpTimeSeries



def power(amp_time_series):
    """
    Computes the square of the norm of a complex number.

    Args:
        amp_time_series (numpy.ndarray): Amplitude time series.

    Returns:
        numpy.ndarray: Square of the norm of the input complex numbers.
    """
    return np.square(np.linalg.norm([amp_time_series], axis=0))


def norm(a, per_channel=False, func=None, **kwargs):
    """
    Computes the norm of a numpy array or dictionary of numpy arrays.

    Args:
        a (Union[numpy.ndarray, dict]): Input array or dictionary of arrays.
        per_channel (bool): If True, compute norm per channel (default is False).
        func (callable): Function to apply for computing the norm (default is np.linalg.norm).
        **kwargs: Additional keyword arguments for the norm function.

    Returns:
        Union[numpy.ndarray, dict]: Norm of the input array or dictionary of arrays.
    """
    if not func:
        func = np.linalg.norm
    
    if per_channel:
        if isinstance(a, (dict, CircAmpTimeSeries)):
            norm_a = {}
            for key, value in a.items():
                norm_a[key] = func(value, **kwargs)
        else:
            raise ValueError("Input must be `dict` or `CircAmpTimeSeries` if per-channel = True")
    else:
        norm_a = func(a, **kwargs)
    
    return norm_a


def dist(a, b, normalize=False, func=None, **kwargs):
    """
    Computes the distance between two numpy arrays or between a number and a numpy array.

    Args:
        a (Union[int, float, complex, numpy.ndarray]): First input array or number.
        b (Union[numpy.ndarray, list]): Second input array or list of arrays.
        normalize (bool): If True, normalize the distance (default is False).
        func (callable): Function to apply for computing the distance (default is np.linalg.norm).
        **kwargs: Additional keyword arguments for the norm function.

    Returns:
        numpy.ndarray: Distance between the input arrays or number and array.
    """
    if isinstance(a, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)) and isinstance(b[0], (list, np.ndarray)): # b is a list
        return [dist(a, b_per, normalize=normalize, func=func, **kwargs) for b_per in b]
    elif isinstance(a, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)):
        if len(a) < len(b):
            a = np.concatenate((a, np.zeros(len(b) - len(a))))
        else:
            b = np.concatenate((b, np.zeros(len(a) - len(b))))
        
        dist_value = norm(a - b, func=func, **kwargs)

    elif isinstance(a, (int, float, complex)) and isinstance(b, (list, np.ndarray)) and isinstance(b[0], (int, float, complex)):
        dist_value = norm([a - np.array(b)], func=func, axis=0, **kwargs)
    elif isinstance(a, (int, float, complex)) and isinstance(b, (int, float, complex)):
        dist_value = norm(a - b, func=func, **kwargs)
    else:
        raise ValueError("Input is of wrong type")
    
    if normalize:
        dist_value /= norm(np.array(a), func=func, **kwargs)

    return dist_value


def circ_dist(a, b, backend, normalize=False, total_func=None, total_args=None, dist_func=None, dist_args=None):
    """
    Computes the distance between two QuantumCircuit objects represented as amplitude time series.

    Args:
        a (QuantumCircuit): First input quantum circuit.
        b (QuantumCircuit): Second input quantum circuit.
        backend (Backend): Backend object for amplitude time series computation.
        normalize (bool): If True, normalize the distance (default is False).
        total_func (callable): Function to apply for computing total amplitude time series.
        total_args (dict): Additional keyword arguments for the total amplitude time series function.
        dist_func (callable): Function to apply for computing the distance.
        dist_args (dict): Additional keyword arguments for the distance function.

    Returns:
        numpy.ndarray: Distance between the input quantum circuits represented as amplitude time series.
    """
    if not isinstance(a, QuantumCircuit) or not isinstance(b, QuantumCircuit):
        raise ValueError("Input must be `qiskit.QuantumCircuit`")
    
    if total_args is None:
        total_args = {}
    if dist_args is None:
        dist_args = {}
    
    total_a = CircAmpTimeSeries.from_circ(a, backend).total(func=total_func, **total_args)
    total_b = CircAmpTimeSeries.from_circ(b, backend).total(func=total_func, **total_args)

    return dist(total_a, total_b, normalize=normalize, func=dist_func, **dist_args)


def min_circ_dist_in_list(circ_list, backend, normalize=False, total_func=None, total_args=None, dist_func=None, dist_args=None):
    """
    Finds the minimum distance between QuantumCircuit objects in a list.

    Args:
        circ_list (list[QuantumCircuit]): List of input quantum circuits.
        backend (Backend): Backend object for amplitude time series computation.
        normalize (bool): If True, normalize the distance (default is False).
        total_func (callable): Function to apply for computing total amplitude time series.
        total_args (dict): Additional keyword arguments for the total amplitude time series function.
        dist_func (callable): Function to apply for computing the distance.
        dist_args (dict): Additional keyword arguments for the distance function.

    Returns:
        Tuple[float, Tuple[int, int]]: Minimum distance and indices of the pair of quantum circuits.
    """
    if total_args is None:
        total_args = {}
    if dist_args is None:
        dist_args = {}
    
    min_circ_dist = float("inf")
    for i, circ in enumerate(circ_list[:-1]):
        circ_dist_list = [circ_dist(circ, c, backend=backend, normalize=False, total_func=total_func, total_args=total_args, dist_func=dist_func, dist_args=dist_args) for c in circ_list[i+1:]]
        curr_min_idx = np.argmin(circ_dist_list)
        curr_min = circ_dist_list[curr_min_idx]
        if normalize:
            normalized_curr_min_1 = curr_min / norm(CircAmpTimeSeries.from_circ(circ, backend).total(func=total_func, **total_args), func=dist_func, **dist_args)
            normalized_curr_min_2 = curr_min / norm(CircAmpTimeSeries.from_circ(circ_list[i+1+curr_min_idx], backend).total(func=total_func, **total_args), func=dist_func, **dist_args)
            if normalized_curr_min_1 < min_circ_dist or normalized_curr_min_2 < min_circ_dist:
                if normalized_curr_min_1 < normalized_curr_min_2:
                    min_idx_pair = (i, i + 1 + curr_min_idx)
                    min_circ_dist = normalized_curr_min_1
                else:
                    min_idx_pair = (i + 1 + curr_min_idx, i)
                    min_circ_dist = normalized_curr_min_2
        else:
            if curr_min < min_circ_dist:
                min_idx_pair = (i, i + 1 + curr_min_idx)
                min_circ_dist = curr_min
    
    return min_circ_dist, min_idx_pair

def partial_reconstruction_metric(retrieved_amp_time_series, data_amp_time_series_list, **kwargs):
    """
    Computes the partial reconstruction metric for retrieved amplitude time series against a list of data amplitude time series.

    Args:
        retrieved_amp_time_series (numpy.ndarray): Retrieved amplitude time series.
        data_amp_time_series_list (Union[numpy.ndarray, list]): List of data amplitude time series.
        **kwargs: Additional keyword arguments for the norm function.

    Returns:
        numpy.ndarray: Partial reconstruction metric for each data amplitude time series.
    """
    if isinstance(data_amp_time_series_list[0], np.ndarray):
        return np.array([norm(retrieved_amp_time_series, data_amp_time_series, **kwargs) for data_amp_time_series in data_amp_time_series_list])
    elif isinstance(data_amp_time_series_list, np.ndarray):
        return np.array(norm(retrieved_amp_time_series, data_amp_time_series_list, **kwargs))