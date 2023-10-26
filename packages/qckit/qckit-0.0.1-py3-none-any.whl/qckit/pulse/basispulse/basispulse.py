import numpy as np
from qiskit.pulse import Schedule
from qiskit.pulse.library.symbolic_pulses import Constant, Drag, Gaussian, GaussianSquare
from ..channel import channel_rep
from ..amptimeseries import CircAmpTimeSeries

class BasisPulse:
    """
    Class for handling basis pulses and their amplitude time series on a specific quantum backend.

    Attributes:
        backend (Backend): The quantum backend for which basis pulses are defined.
        use_channel (bool): If True, channel names in amplitude time series dictionary are `Channel` objects; otherwise, they are strings.
        cmd_def (dict): Command definition dictionary containing basis pulse schedules.
        num_basis_gates (int): Number of basis gates defined for the backend.
        basis_amp_time_series_list (list): List of amplitude time series for basis pulses.
    """

    def __init__(self, backend, use_channel=False):
        """
        Initializes a BasisPulse object.

        Args:
            backend (Backend): The quantum backend for which basis pulses are defined.
            use_channel (bool): If True, channel names in amplitude time series dictionary are `Channel` objects; otherwise, they are strings.
        """
        self.backend = backend
        self.cmd_def = backend.defaults().to_dict()['cmd_def']
        self.num_basis_gates = len(self.cmd_def)
        self.basis_amp_time_series_list = None
        self.use_channel = use_channel

    def schedule_to_amp_time_series(self, sched):
        """
        Converts a Qiskit pulse Schedule object to amplitude time series.

        Args:
            sched (Schedule): Qiskit pulse Schedule object.

        Returns:
            dict: A dictionary containing the amplitude time series for each channel.
        """
        if isinstance(sched, Schedule):
            sched_list = sched.instructions

            amp_time_series_dict = {}
            max_stop_time = 0
            for t0, play_obj in sched_list:
                try:
                    ch = play_obj.channel
                    pulse_amp_time_series = play_obj.pulse.get_waveform().samples
                except AttributeError:
                    continue
                pulse_to_add = np.append(np.zeros(t0, dtype="complex"), pulse_amp_time_series)

                ch = channel_rep(ch, use_channel=self.use_channel)

                if ch not in amp_time_series_dict.keys():
                    amp_time_series_dict[ch] = pulse_to_add
                elif len(amp_time_series_dict[ch]) < len(pulse_to_add):
                    amp_time_series_dict[ch] = np.append(amp_time_series_dict[ch], np.zeros(len(pulse_to_add) - len(amp_time_series_dict[ch]), dtype="complex")) + pulse_to_add
                else:
                    amp_time_series_dict[ch] = amp_time_series_dict[ch] + np.append(pulse_to_add, np.zeros(len(amp_time_series_dict[ch]) - len(pulse_to_add), dtype="complex"))

                if len(amp_time_series_dict[ch]) > max_stop_time:
                    max_stop_time = len(amp_time_series_dict[ch])

            # make amp time_series over all channels to be the same length
            amp_time_series_dict = CircAmpTimeSeries.pad_amp_time_series_dict(amp_time_series_dict)

        return amp_time_series_dict



    def _sched_sequence_to_basis_amp_time_series(self, sched_sequence, total = False, func = None, convert_channel = True):
        """transform 'sequence' metadata provided by IBM in `backend.defaults().to_dict()['cmd_def']` into `amp_time_series` for basis pulses.

        Args:
            sched_sequence (dict): 'sequence' metadata provided by IBM in `backend.defaults().to_dict()['cmd_def']`
            total (bool, optional): whether to get the total `amp_time_series` for baisc pulses. Defaults to False.
            func (callable, optional): a callable object specifying how to calculate the total `amp_time_series`. 
                    Defaults to None, which uses `total_real_abs`, i.e., the sum of the absolute value of the 
                    real part of pulses.

        Returns:
            dict, numpy.array: if `total = False`, returns a `dict` whose key is the channel and value is `amp_time_series`
                    on that channel. Note that the length of `amp_time_series` is made to be the same. Otherwise, returns
                    an `numpy.array` which is the amp_time_series for that `sched_sequence`.
        """
        # keep track of the maximum length of amp_time_series, in order to make 
        # amp_time_series over all channels have the same length
        max_sched_end_time = 0 
        amp_time_series_dict = {}
        for sched in sched_sequence:
            if 'pulse_shape' in sched.keys():
                if 'ch' in sched.keys():
                    ch = sched['ch']
                    channel = channel_rep(ch, use_channel=self.use_channel)
                    
                    # append 0 to the start 
                    if channel not in amp_time_series_dict.keys():
                        amp_time_series_dict[channel] = np.zeros(sched['t0'], dtype = "complex")
                    
                    # add 0 to the start
                    try:
                        sched_duration = sched['parameters']['duration']
                    except KeyError:
                        sched_duration = 0
                    sched_end_time = sched['t0'] + sched_duration
                    max_sched_end_time = max(max_sched_end_time, sched_end_time)
                    if len(amp_time_series_dict[channel]) < sched_end_time:
                        amp_time_series_dict[channel] = np.append(amp_time_series_dict[channel], np.zeros(sched_end_time - len(amp_time_series_dict[channel])))
                    
                    pulse_shape = sched['pulse_shape']
                    if pulse_shape == 'constant':
                        amp_time_series_dict[channel][sched['t0']:sched_end_time] = Constant(**sched['parameters']).get_waveform().samples
                    elif pulse_shape == 'drag':
                        amp_time_series_dict[channel][sched['t0']:sched_end_time] = Drag(**sched['parameters']).get_waveform().samples
                    elif pulse_shape == 'gaussian':
                        amp_time_series_dict[channel][sched['t0']:sched_end_time] = Gaussian(**sched['parameters']).get_waveform().samples
                    elif pulse_shape == 'gaussian_square':
                        amp_time_series_dict[channel][sched['t0']:sched_end_time] = GaussianSquare(**sched['parameters']).get_waveform().samples
                    else:
                        raise ValueError("Pulse shape is not found!")
        
        # make amp_time_series over all channels have the same length
        amp_time_series_dict = CircAmpTimeSeries.pad_amp_time_series_dict(amp_time_series_dict)

        if total:
            if not func:
                def total_func(amp_time_series_dict):
                    total_value = np.zeros(len(list(amp_time_series_dict.values())[0]))
                    for amp_time_series in amp_time_series_dict.values():
                        total_value += np.linalg.norm([amp_time_series], axis=0)
                    return total_value
                func = total_func
            return func(amp_time_series_dict)
        else:
            return amp_time_series_dict



    def get_basis_amp_time_series_list(self, total=False, func=None):
        """
        Get the list of amplitude time series for basis pulses.

        Args:
            total (bool, optional): If True, returns the total amplitude time series over all channels for each basis pulse. Defaults to False.
            func (callable, optional): A callable object specifying how to calculate the total amplitude time series. Defaults to None, which uses `total_real_abs`, i.e., the sum of the absolute value of the real part of pulses.

        Returns:
            list: A list containing dictionaries with basis pulse name, qubits, and corresponding amplitude time series.
        """
        if self.basis_amp_time_series_list:
            return self.basis_amp_time_series_list
        else:
            amp_time_series_list = []
            for basis_gate_sched in self.cmd_def:
                amp_time_series = {}
                amp_time_series['name'] = basis_gate_sched['name']
                amp_time_series['qubits'] = basis_gate_sched['qubits']
                amp_time_series['amp_time_series'] = self._sched_sequence_to_basis_amp_time_series(basis_gate_sched['sequence'], total=total, func=func)
                amp_time_series_list.append(amp_time_series)
            self.basis_amp_time_series_list = amp_time_series_list
            return amp_time_series_list

    def get_basis_gate_schedule(self, instruction, qubits, *params, **kwparams):
        """
        Get the basis gate schedule for the specified instruction and qubits.

        Args:
            instruction (str): The name of the basis gate.
            qubits (list): List of qubits to which the basis gate is applied.
            *params: Additional parameters for the basis gate.
            **kwparams: Additional keyword parameters for the basis gate.

        Returns:
            Schedule: The basis gate schedule.
        """
        return self.backend.defaults().instruction_schedule_map.get(instruction, qubits, *params, **kwparams)

    def get_basis_gate_parameters(self, instruction, qubits, *params, **kwparams):
        """
        Get the parameters for the specified basis gate and qubits.

        Args:
            instruction (str): The name of the basis gate.
            qubits (list): List of qubits to which the basis gate is applied.
            *params: Additional parameters for the basis gate.
            **kwparams: Additional keyword parameters for the basis gate.

        Returns:
            dict: A dictionary containing the parameters for the basis gate.
        """
        sched = self.get_basis_gate_schedule(instruction, qubits, *params, **kwparams)
        sched_list = sched.instructions

        param_dict = {}
        for t0, play_obj in sched_list:
            try:
                ch = play_obj.channel
                ch = channel_rep(ch, use_channel=self.use_channel)
                parameters = play_obj.pulse.parameters
                parameters['t0'] = t0
                if ch in param_dict.keys():
                    param_dict[ch].append(parameters)
                else:
                    param_dict[ch] = [parameters]
            except AttributeError:
                continue

        return param_dict

    def get_basis_amp_time_series(self, instruction, qubits, *params, **kwparams):
        """
        Get the amplitude time series for the specified basis gate and qubits.

        Args:
            instruction (str): The name of the basis gate.
            qubits (list): List of qubits to which the basis gate is applied.
            *params: Additional parameters for the basis gate.
            **kwparams: Additional keyword parameters for the basis gate.

        Returns:
            dict: A dictionary containing the amplitude time series for the specified basis gate and qubits.
        """
        sched = self.get_basis_gate_schedule(instruction, qubits, *params, **kwparams)
        return self.schedule_to_amp_time_series(sched)

    def save_basis_amp_time_series_list(self, filename=None):
        """
        Save the basis amplitude time series list to a pickle file.

        Args:
            filename (str, optional): The filename to save the basis amplitude time series list. If None, uses the backend name as the filename. Defaults to None.
        """
        import pickle

        if not filename:
            filename = self.backend.name()

        with open(filename, "wb") as f:
            pickle.dump(self.get_basis_amp_time_series_list(), f)

    @staticmethod
    def load_basis_amp_time_series_list(filename):
        """
        Load the basis amplitude time series list from a pickle file.

        Args:
            filename (str): The filename from which to load the basis amplitude time series list.

        Returns:
            list: A list containing dictionaries with basis pulse name, qubits, and corresponding amplitude time series.
        """
        import pickle

        with open(filename, "rb") as f:
            return pickle.load(f)

if __name__ == "__main__":
    from qcutils.credential import load_provider
    provider = load_provider()
    backend = provider.get_backend("ibmq_jakarta")

    bp = BasisPulse(backend)
    basis_amp_time_series_list = bp.get_basis_amp_time_series_list(total=True)
    print(basis_amp_time_series_list)