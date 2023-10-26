from qcutils.pulse.amptimeseries import circ_to_amp_time_series
import numpy as np

class PulseMetric:
    """
    A class for computing pulse metrics for a set of circuits.

    Attributes:
        _benchmark (Benchmark): A benchmark object containing the circuits to compute pulse metrics for.
        _circ_name_list (list[str]): A list of circuit names.
        _circ_list (list[QuantumCircuit]): A list of circuits.
        _backend (BaseBackend): The backend to use for computing pulse metrics.
    """
    def __init__(self, benchmark, backend):
        """
        Initializes a PulseMetric object.

        Args:
            benchmark (Benchmark): A benchmark object containing the circuits to compute pulse metrics for.
            backend (BaseBackend): The backend to use for computing pulse metrics.
        """
        self._benchmark = benchmark
        self._circ_name_list = benchmark.circ_name_list
        self._circ_list = benchmark.circ_list
        self._backend = backend
    
    @property
    def circ_list(self):
        """
        Returns:
            list[QuantumCircuit]: A list of circuits.
        """
        return self._circ_list
    
    @property
    def circ_name_list(self):
        """
        Returns:
            list[str]: A list of circuit names.
        """
        return self._circ_name_list
    
    def to_amp_timeseries_dict(self, scale = 1, total = False, func = None, do_transpile = True, **transpiler_args):
        """
        Computes the amplitude time series for each circuit in the benchmark.

        Args:
            scale (float): A scaling factor for the amplitude time series.
            total (bool): If True, computes the total amplitude time series for each circuit.
            func (function): A function to apply to the amplitude time series.
            do_transpile (bool): If True, transpiles the circuits before computing the amplitude time series.
            **transpiler_args: Additional arguments to be passed to the transpiler.

        Returns:
            dict: A dictionary mapping circuit names to amplitude time series.
        """
        amp_timeseries_dict = {}
        for circ_name, circ in zip(self._circ_name_list, self._circ_list):
            try:
                amp_timeseries_dict[circ_name] = circ_to_amp_time_series(circ, self._backend, scale=scale, total=total, func=func, do_transpile=do_transpile, **transpiler_args)
            finally:
                continue
        return amp_timeseries_dict

    def to_mean_amp_timeseries_dict(self, scale = 1, func = None, do_transpile = True, **transpiler_args):
        """
        Computes the mean amplitude time series for each circuit in the benchmark.

        Args:
            scale (float): A scaling factor for the amplitude time series.
            func (function): A function to apply to the amplitude time series.
            do_transpile (bool): If True, transpiles the circuits before computing the amplitude time series.
            **transpiler_args: Additional arguments to be passed to the transpiler.

        Returns:
            dict: A dictionary mapping circuit names to mean amplitude time series.
        """
        amp_timeseries_dict = {}
        for circ_name, circ in zip(self._circ_name_list, self._circ_list):
            try:
                amp_timeseries_dict[circ_name] = np.mean(circ_to_amp_time_series(circ, self._backend, scale=scale, total=True, func=func, do_transpile=do_transpile, **transpiler_args))
            finally:
                continue
        return amp_timeseries_dict
