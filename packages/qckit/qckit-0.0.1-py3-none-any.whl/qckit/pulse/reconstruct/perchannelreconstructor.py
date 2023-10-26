import numpy as np
from qiskit.pulse.channels import DriveChannel, ControlChannel
from ..basispulse.basispulse import BasisPulse
from ..amptimeseries import CircAmpTimeSeries
from ..amptimeseries.metric import power as power_func
from ..channel import channel_rep

class PerChannelReconstructor:
    """
    A class for reconstructing amplitude time series data from quantum circuits based on basis pulses.
    """
    def __init__(self, backend, boundary=None, tolerance=None, use_channel=False) -> None:
        """
        Initializes the PerChannelReconstructor object.
        
        Args:
            backend (object): Backend object providing configuration details.
            boundary (float, optional): Threshold for considering amplitudes. Defaults to 0.02.
            tolerance (int, optional): Tolerance value for comparison. Defaults to 2.
            use_channel (bool, optional): Flag to specify the use of channels. Defaults to False.
        """
        self.backend = backend
        if not boundary:
            boundary = 0.02
        self.boundary = boundary
        if not tolerance:
            tolerance = 2
        self.tolerance = tolerance
        self.use_channel = use_channel
        self.basis_pulse = BasisPulse(backend, use_channel=False)
        self.granularity = backend.configuration().timing_constraints['granularity']
        self.basis_gate_start_end = self.get_basis_gate_start_end(power=True)
        self.basis_gate_length_bound = self.get_basis_gate_length(power=True)
        self.basis_gate_length = self.get_basis_gate_length(boundary=0, power=True)
    

    def get_basis_gate_start_end(self, boundary=None, power=False):
        """
        Determines the start and end points of basis gates.

        Args:
            boundary (float, optional): Threshold for considering amplitudes. Defaults to self.boundary.
            power (bool, optional): Flag to specify using power function. Defaults to False.

        Returns:
            dict: Dictionary containing basis gate start and end points.
        """
        if boundary == None:
            boundary = self.boundary
        basis_amp_time_series_list = self.basis_pulse.get_basis_amp_time_series_list()
        # amp_time_series_dict to power
        basis_gate_start_end_dict = {}
        for basis_gate in basis_amp_time_series_list:
            if basis_gate['name'] not in basis_gate_start_end_dict.keys():
                basis_gate_start_end_dict[basis_gate['name']] = {}
            
            segment_list = []
            if basis_gate['name'] == 'cx':
                # only add control length for cx
                for channel, amp_time_series in basis_gate['amp_time_series'].items():
                    ch = channel_rep(channel, use_channel=self.use_channel)
                    if channel[0] == 'u' or isinstance(channel, ControlChannel):
                        if power:
                            amp_time_series = power_func(amp_time_series)
                        segment_list.append(self.get_binary_segment(amp_time_series, boundary=boundary))
                        if ch in basis_gate_start_end_dict[basis_gate['name']].keys():
                            basis_gate_start_end_dict[basis_gate['name']][ch].append(segment_list)
                        else:
                            basis_gate_start_end_dict[basis_gate['name']][ch] = [segment_list]
            elif basis_gate['name'] in ['sx', 'x']:
                for channel, amp_time_series in basis_gate['amp_time_series'].items():
                    if power:
                        amp_time_series = power_func(amp_time_series)
                    ch = channel_rep(channel, use_channel=self.use_channel)
                    segment_list.append(self.get_binary_segment(amp_time_series, boundary=boundary))
                    basis_gate_start_end_dict[basis_gate['name']][ch] = segment_list
            else:
                continue
            
        return basis_gate_start_end_dict
    

    def get_basis_gate_length(self, boundary=None, power=False):
        """
        Calculates the lengths of basis gates.

        Args:
            boundary (float, optional): Threshold for considering amplitudes. Defaults to self.boundary.
            power (bool, optional): Flag to specify using power function. Defaults to False.

        Returns:
            dict: Dictionary containing basis gate lengths.
        """
        if boundary == None:
            boundary = self.boundary
        basis_gate_start_end_dict = self.get_basis_gate_start_end(boundary=boundary, power=power)
        basis_gate_length_dict = {}
        for gate_name, start_end_dict in basis_gate_start_end_dict.items():
            if gate_name in ['sx', 'x']:
                basis_gate_length_dict[gate_name] = {}
                for channel, start_end_list in start_end_dict.items():
                    channel = channel_rep(channel, use_channel=self.use_channel)
                    if len(start_end_list[0][0]) > 0:
                        length = start_end_list[0][0][1] - start_end_list[0][0][0] + 1 
                    else:
                        length = 0
                    basis_gate_length_dict[gate_name][channel] = length
            elif gate_name in ['cx']:
                basis_gate_length_dict[gate_name] = {}
                for channel, start_end_dict_i in start_end_dict.items():
                    for start_end_list in start_end_dict_i:
                        channel_rep(channel, use_channel=self.use_channel)
                        # [length1, interval, length2]
                        if len(start_end_list[0][0]) > 0:
                            length_list = []
                            for i, (start, end) in enumerate(start_end_list[0]):
                                length_list.append(end - start + 1) # length
                                if i + 1 < len(start_end_list[0]):
                                    length_list.append(start_end_list[0][i+1][0] - start_end_list[0][i][1] + 1) #interval
                        else:
                            length_list = []
                        if channel in basis_gate_length_dict[gate_name].keys():
                            basis_gate_length_dict[gate_name][channel].append(length_list)
                        else:
                            basis_gate_length_dict[gate_name][channel] = [length_list]
                    
        return basis_gate_length_dict


    @staticmethod
    def binarize_amp_time_series_dict(amp_time_series_dict, boundary):
        """
        Binarizes amplitude time series data based on a given threshold.

        Args:
            amp_time_series_dict (dict): Dictionary containing amplitude time series data.
            boundary (float): Threshold for binarization.

        Returns:
            dict: Binarized amplitude time series data.
        """
        for channel, amp_time_series in amp_time_series_dict:
            amp_time_series_dict[channel] = amp_time_series >= boundary
        return amp_time_series_dict
    

    @staticmethod
    def get_binary_segment(amp_time_series, boundary):
        """
        Extracts binary segments from amplitude time series data.

        Args:
            amp_time_series (array): Amplitude time series data.
            boundary (float): Threshold for binarization.

        Returns:
            list: List of binary segments.
        """
        if len(amp_time_series):
            binary_array = np.abs(amp_time_series) >= boundary

            starts = np.where(np.diff(np.concatenate(([0], binary_array, [0]))) == 1)[0]
            ends = np.where(np.diff(np.concatenate(([0], binary_array, [0]))) == -1)[0] - 1

            start_end_list = list(zip(starts, ends))
            if len(start_end_list) > 0:
                return start_end_list
            else:
                return [()]
        else:
            return [()]
    


    def remove_gate_from_circ_amp_time_series(self, circ_amp_time_series, instruction, qubits, t0):
        """
        Removes a gate from circuit amplitude time series data.

        Args:
            circ_amp_time_series (CircAmpTimeSeries): Circuit amplitude time series data.
            instruction (str): Gate instruction name.
            qubits (list): List of qubits involved in the gate.
            t0 (int): Time step for gate removal.

        Returns:
            CircAmpTimeSeries: Updated circuit amplitude time series data.
        """
        gate_pulse_dict = self.basis_pulse.get_basis_amp_time_series(instruction, qubits)
        for channel, amp_time_series in gate_pulse_dict.items():
            channel = channel_rep(channel, use_channel=self.use_channel)
            if channel in circ_amp_time_series.keys():
                if len(circ_amp_time_series[channel]) - t0 - len(amp_time_series) >= 0:
                    circ_amp_time_series[channel] -= np.concatenate((np.zeros(t0), amp_time_series, np.zeros(len(circ_amp_time_series[channel]) - t0 - len(amp_time_series))))
                else:
                    raise ValueError("t0 cannot be less than 0")
        return circ_amp_time_series


    def _to_closest_granularity(self, value):
        """
        Rounds the given value to the closest granularity.

        Args:
            value (float): Value to be rounded.

        Returns:
            float: Rounded value to the closest granularity.
        """
        if value / self.granularity - int(value / self.granularity) > 0.5:
            return (int(value / self.granularity) + 1) * self.granularity
        else:
            return int(value / self.granularity) * self.granularity
        
    
    def _channel_to_qubits(self, channel):
        """
        Maps channel to qubits based on backend configuration.

        Args:
            channel (str): Channel name.

        Returns:
            list: List of qubits associated with the channel.
        """
        return self.backend.configuration().to_dict()["channels"][channel]['operates']['qubits']


    def remove_multiqubit_pulse(self, circ_amp_time_series):
        """
        Removes multi-qubit pulses from the circuit amplitude time series.

        Args:
            circ_amp_time_series (CircAmpTimeSeries): Circuit amplitude time series data.

        Returns:
            tuple: Updated circuit amplitude time series and list of removed multi-qubit pulses.
        """
        cx_list = []
        for channel, amp_time_series in circ_amp_time_series.items():
            if isinstance(channel, str) and channel[0] == 'u' and channel in self.basis_gate_length['cx'].keys():
                cx_gate_length = self.basis_gate_length['cx'][channel][0]
                cx_gate_start_interval_end = self.basis_gate_length_bound['cx'][channel]
                binarized_segment = PerChannelReconstructor.get_binary_segment(power_func(amp_time_series), self.boundary)
                qubits = self._channel_to_qubits(channel)
                if len(binarized_segment) > 1:
                    for i in range(0, len(binarized_segment), 2):
                        if i + 1 < len(binarized_segment):
                            start_1 = binarized_segment[i][0]
                            end_1 = binarized_segment[i][1]
                            start_2 = binarized_segment[i+1][0]
                            end_2 = binarized_segment[i+1][1]

                            exist_1 = False
                            exist_2 = False
                            if end_1 - start_1 + self.tolerance > cx_gate_start_interval_end[0][0] and \
                                start_2 - end_1 + self.tolerance > cx_gate_start_interval_end[0][1] and \
                                end_2 - start_2 + self.tolerance > cx_gate_start_interval_end[0][2]:
                                t0 = binarized_segment[i][0] - self.basis_gate_start_end['cx'][channel][0][0][0][0]
                                t0 = self._to_closest_granularity(t0)
                                amp_time_series_dict_1 = circ_amp_time_series.deepcopy()
                                try:
                                    amp_time_series_dict_1 = self.remove_gate_from_circ_amp_time_series(amp_time_series_dict_1, 'cx', qubits, t0)
                                    total_power_1 = np.sum([power_func(a) for a in amp_time_series_dict_1.values()])
                                    exist_1 = True
                                except ValueError:
                                    pass
                            if end_1 - start_1 + self.tolerance > cx_gate_start_interval_end[1][0] and \
                                start_2 - end_1 + self.tolerance > cx_gate_start_interval_end[1][1] and \
                                end_2 - start_2 + self.tolerance > cx_gate_start_interval_end[1][2]:
                                t0 = binarized_segment[i][0] - self.basis_gate_start_end['cx'][channel][1][0][0][0]
                                t0 = self._to_closest_granularity(t0)
                                amp_time_series_dict_2 = circ_amp_time_series.deepcopy()
                                try:
                                    amp_time_series_dict_2 = self.remove_gate_from_circ_amp_time_series(amp_time_series_dict_2, 'cx', [qubits[1], qubits[0]], t0)
                                    total_power_2 = np.sum([power_func(a) for a in amp_time_series_dict_2.values()])
                                    exist_2 = True
                                except ValueError:
                                    pass
                            else:
                                continue
                            if (exist_1 and not exist_2) or (exist_1 and exist_2 and total_power_1 <= total_power_2):
                                circ_amp_time_series = amp_time_series_dict_1
                                cx_list.append([t0, 'cx', qubits])
                            elif (not exist_1 and exist_2) or (exist_1 and exist_2 and total_power_1 > total_power_2):
                                circ_amp_time_series = amp_time_series_dict_2
                                cx_list.append([t0, 'cx', [qubits[1], qubits[0]]])
                        else:
                            raise Exception("TODO")

        return circ_amp_time_series, cx_list


    def remove_singlequbit_pulse(self, circ_amp_time_series, instruction):
        """
        Removes single-qubit pulses from the circuit amplitude time series based on the given instruction.

        Args:
            circ_amp_time_series (CircAmpTimeSeries): Circuit amplitude time series data.
            instruction (str): Single-qubit instruction name.

        Returns:
            tuple: Updated circuit amplitude time series and list of removed single-qubit pulses.
        """
        singlequbit_gate_list = []
        for channel, amp_time_series in circ_amp_time_series.items():
            if isinstance(channel, str) and channel[0] == 'd' and channel in self.basis_gate_length[instruction].keys():
                singlequbit_gate_length = self.basis_gate_length[instruction][channel]
                singlequbit_gate_length_bound = self.basis_gate_length_bound[instruction][channel]
                binarized_segment = PerChannelReconstructor.get_binary_segment(power_func(amp_time_series), self.boundary)
                if binarized_segment[0]:
                    for start, end in binarized_segment:
                        if end - start + self.tolerance >= singlequbit_gate_length_bound and \
                            end - start - self.tolerance <= singlequbit_gate_length_bound:
                            t0 = start - self.basis_gate_start_end[instruction][channel][0][0][0]
                        else:
                            continue
                        t0 = self._to_closest_granularity(t0)
                        qubits = self._channel_to_qubits(channel)
                        singlequbit_gate_list.append([t0, instruction, qubits])
                        circ_amp_time_series = self.remove_gate_from_circ_amp_time_series(circ_amp_time_series, instruction, qubits, t0)

        return circ_amp_time_series, singlequbit_gate_list

    
    def reconstruct(self, circ_amp_time_series):
        """
        Reconstructs amplitude time series data from circuit amplitude time series.

        Args:
            circ_amp_time_series (CircAmpTimeSeries): Circuit amplitude time series data.

        Returns:
            list: List of reconstructed gate information.
        """
        circ_amp_time_series = circ_amp_time_series.deepcopy()
        circ_amp_time_series, cx_list = self.remove_multiqubit_pulse(circ_amp_time_series)
        circ_amp_time_series, x_list = self.remove_singlequbit_pulse(circ_amp_time_series, "x")
        circ_amp_time_series, sx_list = self.remove_singlequbit_pulse(circ_amp_time_series, "sx")
        return cx_list + sx_list + x_list
    

    def gate_list_to_circ_amp_time_series(self, gate_list):
        """
        Converts a list of gate information to circuit amplitude time series data.

        Args:
            gate_list (list): List of gate information.

        Returns:
            CircAmpTimeSeries: Circuit amplitude time series data.
        """
        circ_amp_time_series = CircAmpTimeSeries({}, self.backend)
        for t0, instruction, qubits in gate_list:
            gate_pulse_dict = self.basis_pulse.get_basis_amp_time_series(instruction, qubits)
            amp_time_series_to_add = {}
            for channel, amp_time_series in gate_pulse_dict.items():
                amp_time_series_to_add[channel_rep(channel, use_channel=self.use_channel)] = np.concatenate((np.zeros(t0), amp_time_series))
            circ_amp_time_series += amp_time_series_to_add
        circ_amp_time_series.pad()
        return circ_amp_time_series
    

    def get_reconstructed_total(self, circ, do_transpile=True, **transplier_args):
        """
        Calculates the total reconstructed amplitude from a quantum circuit.

        Args:
            circ (QuantumCircuit): Quantum circuit.
            do_transpile (bool, optional): Flag to specify if circuit should be transpiled. Defaults to True.

        Returns:
            float: Total reconstructed amplitude.
        """
        circ_amp_time_series = CircAmpTimeSeries.from_circ(circ, self.backend, do_transpile=do_transpile, **transplier_args)
        gate_list = self.reconstruct(circ_amp_time_series)
        total_reconstruct = self.gate_list_to_circ_amp_time_series(gate_list).total()
        return total_reconstruct
