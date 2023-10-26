from .amptimeseries import sched_to_amp_time_series, circ_to_amp_time_series
from ..channel import channel_rep
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.pulse import Schedule
import numpy as np



class CircAmpTimeSeries:
    """
    A class for working with amplitude time series for a `QuantumCircuit` object.

    Attributes:
        backend (Backend): The backend to use for transpilation and scheduling.
        use_channel (bool): If True, the channel names in the amplitude time series dictionary are `Channel` objects; otherwise, they are strings.
        _amp_time_series_dict (Dict[Union[Channel, str], numpy.ndarray]): A dictionary containing the amplitude time series for each channel.
    """

    _dtype = "complex"

    def __init__(self, amp_time_series_dict, backend, use_channel = False):
        """
        Initializes a `CircAmpTimeSeries` object.

        Args:
            amp_time_series_dict (Dict[Union[Channel, str], numpy.ndarray]): A dictionary containing the amplitude time series for each channel.
            backend (Backend): The backend to use for transpilation and scheduling.
            use_channel (bool): If True, the channel names in the amplitude time series dictionary are `Channel` objects; otherwise, they are strings.
        """
        self.backend = backend
        self.use_channel = use_channel
        self._amp_time_series_dict = CircAmpTimeSeries.parse_amp_time_series_dict(amp_time_series_dict, use_channel=use_channel)


    def deepcopy(self):
        """
        Returns a deep copy of the `CircAmpTimeSeries` object.

        Returns:
            CircAmpTimeSeries: A deep copy of the `CircAmpTimeSeries` object.
        """
        # faster than copy.deepcopy
        return CircAmpTimeSeries(self._amp_time_series_dict, self.backend, use_channel=self.use_channel)


    @property
    def amp_time_series_dict(self):
        """
        Returns the amplitude time series dictionary.

        Returns:
            Dict[Union[Channel, str], numpy.ndarray]: The amplitude time series dictionary.
        """
        return self._amp_time_series_dict


    @staticmethod
    def pad_amp_time_series_dict(amp_time_series_dict):
        """
        Pads the amplitude time series in a dictionary with zeros so that they are all the same length.

        Args:
            amp_time_series_dict (Dict[str, numpy.ndarray]): A dictionary of amplitude time series, where the keys are
                channel names and the values are one-dimensional numpy arrays of complex numbers.

        Returns:
            Dict[str, numpy.ndarray]: The padded dictionary of amplitude time series.
        """
        # Find the maximum length of the amplitude time series
        if len(amp_time_series_dict):
            max_len = max([len(x) for x in amp_time_series_dict.values()])
            # Pad each amplitude time series with zeros so that they are all the same length
            for channel, amp_time_series in amp_time_series_dict.items():
                if len(amp_time_series) < max_len:
                    amp_time_series_dict[channel] = np.concatenate((amp_time_series, np.zeros(max_len - len(amp_time_series))))
                # Convert the amplitude time series to the appropriate data type
                amp_time_series_dict[channel] = np.array(amp_time_series_dict[channel], dtype=CircAmpTimeSeries._dtype)
        return amp_time_series_dict
    
    



    def pad(self):
        """
        Pads the amplitude time series in the object's dictionary with zeros so that they are all the same length.
        """
        # Find the maximum length of the amplitude time series
        max_len = max([len(x) for x in self._amp_time_series_dict.values()])
        # Pad each amplitude time series with zeros so that they are all the same length
        for channel, amp_time_series in self._amp_time_series_dict.items():
            if len(amp_time_series) < max_len:
                self._amp_time_series_dict[channel] = np.concatenate((amp_time_series, np.zeros(max_len - len(amp_time_series))))
            # Convert the amplitude time series to the appropriate data type
            self._amp_time_series_dict[channel] = np.array(self._amp_time_series_dict[channel], dtype=CircAmpTimeSeries._dtype)

    @staticmethod
    def parse_amp_time_series_dict(amp_time_series_dict, use_channel=False):
        """
        Parses and pads the input amplitude time series dictionary.

        Args:
            amp_time_series_dict (Dict[Union[Channel, str], numpy.ndarray]): A dictionary containing the amplitude time series for each channel.
            use_channel (bool): If True, the channel names in the amplitude time series dictionary are `Channel` objects; otherwise, they are strings.

        Returns:
            Dict[str, numpy.ndarray]: The parsed and padded dictionary of amplitude time series.
        """
        if isinstance(amp_time_series_dict, dict):
            amp_time_series_dict_parsed = {}
            for channel, amp_time_series in amp_time_series_dict.items():
                if isinstance(amp_time_series, (np.ndarray, list)):
                    channel_str = channel_rep(channel, use_channel=use_channel)
                    amp_time_series_dict_parsed[channel_str] = np.array(amp_time_series, dtype=CircAmpTimeSeries._dtype)
                else:
                    raise ValueError("Values for the 'amp_time_series_dict' must be numpy.ndarray")
        else:
            raise ValueError("'amp_time_series_dict' must be dict whose keys are 'qiskit.pulse.channels.Channel' and values are 'numpy.ndarray'")

        amp_time_series_dict_parsed = CircAmpTimeSeries.pad_amp_time_series_dict(amp_time_series_dict_parsed)
        
        return amp_time_series_dict_parsed

    @staticmethod
    def from_sched(sched, backend):
        """
        Creates a `CircAmpTimeSeries` object from a pulse `Schedule`.

        Args:
            sched (Schedule): The pulse schedule.
            backend (Backend): The backend to use for transpilation and scheduling.

        Returns:
            CircAmpTimeSeries: The `CircAmpTimeSeries` object.
        """
        amp_time_series_dict = sched_to_amp_time_series(sched, total=False, use_channel=False)
        cats = CircAmpTimeSeries(amp_time_series_dict, backend)
        return cats

    @staticmethod
    def from_circ(circ, backend, do_transpile=False, **transpiler_args):
        """
        Creates a `CircAmpTimeSeries` object from a `QuantumCircuit`.

        Args:
            circ (QuantumCircuit): The quantum circuit.
            backend (Backend): The backend to use for transpilation and scheduling.
            do_transpile (bool): Whether to transpile the circuit.

        Returns:
            CircAmpTimeSeries: The `CircAmpTimeSeries` object.
        """
        amp_time_series_dict  = circ_to_amp_time_series(circ, backend, total=False, use_channel=False, do_transpile=do_transpile, **transpiler_args)
        cats = CircAmpTimeSeries(amp_time_series_dict, backend)
        return cats
    

    @staticmethod
    def from_data(data, backend, do_transpile = False, **transpiler_args):
        """
        Creates a `CircAmpTimeSeries` object
        from a given data source (dictionary, Schedule, or QuantumCircuit).

        Args:
            data (Union[dict, Schedule, QuantumCircuit]): The input data.
            backend (Backend): The backend to use for transpilation and scheduling.
            do_transpile (bool): Whether to transpile the circuit if the input is a QuantumCircuit.

        Returns:
            CircAmpTimeSeries: The `CircAmpTimeSeries` object.
        """
        if isinstance(data, dict):
            return CircAmpTimeSeries(data, backend)
        if isinstance(data, Schedule):
            return CircAmpTimeSeries.from_sched(data, backend)
        if isinstance(data, QuantumCircuit):
            return CircAmpTimeSeries.from_circ(data, backend, do_transpile=do_transpile, **transpiler_args)

    def total(self, func=None, per_channel=False, **kwargs):
        """
        Calculates the total amplitude time series.

        Args:
            func (callable): A function to apply to the amplitude time series.
            per_channel (bool): If True, calculate total for each channel separately.

        Returns:
            Union[numpy.ndarray, Dict[str, numpy.ndarray]]: The total amplitude time series.
        """
        if not self._amp_time_series_dict:
            raise ValueError("Have not provided amp_time_series")
        
        if per_channel:
            total_dict = {}
            for channel, amp_time_series in self._amp_time_series_dict.values():
                if not func:
                    total_dict[channel] = np.square(np.linalg.norm([amp_time_series], axis=0))
                else:
                    total_dict[channel] = func(amp_time_series, **kwargs)
            return total_dict
        else:
            if not func:
                return np.square(np.linalg.norm(list(self._amp_time_series_dict.values()), axis=0))
            else:
                return func(list(self._amp_time_series_dict.values()), **kwargs)

    def draw(self, **kwargs):
        """
        Plots the amplitude time series for each channel.

        Args:
            **kwargs: Additional keyword arguments for plotting.
        """
        x_max = max([len(amp_time_series) for amp_time_series in self._amp_time_series_dict.values()])
        for i, (channel, time_series) in enumerate(self._amp_time_series_dict.items()):
            plt.subplot(len(self._amp_time_series_dict), 1, i+1)
            plt.plot(range(len(time_series)), np.real(time_series), label="real", **kwargs)
            plt.plot(range(len(time_series)), np.imag(time_series), label="imag", **kwargs)

            plt.plot([0, x_max], [0, 0], c='grey', linestyle="--")
            plt.xlim([0, x_max])
            plt.ylim([-1, 1])
            plt.title(channel_rep(channel, use_channel=False))
            plt.xlabel("Time Step")
            plt.ylabel("Amp")
            plt.legend()

    def add_noise(self, func=None, **kwargs):
        """
        Adds noise to the amplitude time series.

        Args:
            func (callable): A function to generate noise values (default is numpy.random.normal).
            **kwargs: Additional keyword arguments for the noise generation function.
        """
        if not func:
            func = np.random.normal
        for channel, amp_time_series in self._amp_time_series_dict.items():
            self._amp_time_series_dict[channel] += func(**kwargs)

    def __getitem__(self, channel):
        """
        Returns the amplitude time series for a specific channel.

        Args:
            channel (Union[Channel, str]): The channel.

        Returns:
            numpy.ndarray: The amplitude time series for the specified channel.
        """
        channel = channel_rep(channel, use_channel=self.use_channel)
        if channel in self._amp_time_series_dict.keys():
            return self._amp_time_series_dict[channel]
        else:
            raise KeyError(f"This CircAmpTimeSeries object does not have key {channel}")

    def __setitem__(self, channel, amp_time_series):
        """
        Sets the amplitude time series for a specific channel.

        Args:
            channel (Union[Channel, str]): The channel.
            amp_time_series (numpy.ndarray): The amplitude time series for the specified channel.
        """
        self._amp_time_series_dict[channel] = amp_time_series

    def __delitem__(self, channel):
        """
        Deletes the amplitude time series for a specific channel.

        Args:
            channel (Union[Channel, str]): The channel.
        """
        del self._amp_time_series_dict[channel]

    def __len__(self):
        """
        Returns the number of channels in the `CircAmpTimeSeries` object.

        Returns:
            int: The number of channels.
        """
        return len(list(self._amp_time_series_dict.keys()))

    def __contains__(self, channel):
        """
        Checks if a specific channel is present in the `CircAmpTimeSeries` object.

        Args:
            channel (Union[Channel, str]): The channel.

        Returns:
            bool: True if the channel is present, False otherwise.
        """
        return channel in self._amp_time_series_dict.keys()

    def keys(self):
        """
        Returns the channel names in the `CircAmpTimeSeries` object.

        Returns:
            dict_keys: The channel names.
        """
        return self._amp_time_series_dict.keys()

    def values(self):
        """
        Returns the amplitude time series values in the `CircAmpTimeSeries` object.

        Returns:
            dict_values: The amplitude time series values.
        """
        return self._amp_time_series_dict.values()

    def items(self):
        """
        Returns the channel names and amplitude time series pairs in the `CircAmpTimeSeries` object.

        Returns:
            dict_items: The channel names and amplitude time series pairs.
        """
        return self._amp_time_series_dict.items()

    def __repr__(self):
        """
        Returns a string representation of the `CircAmpTimeSeries` object.

        Returns:
            str: The string representation.
        """
        repr_str = f"""
            backend: {self.backend.configuration().backend_name}
            use_channel: {self.use_channel}
            ---------------------------------------
        \n"""
        for channel, amp_time_series in self._amp_time_series_dict.items():
            repr_str += f"{channel}: {amp_time_series}\n"
        return repr_str

    def __str__(self):
        """
        Returns a human-readable string representation of the `CircAmpTimeSeries` object.

        Returns:
            str: The human-readable string representation.
        """
        return self.__repr__()

    def __neg__(self):
        """
        Returns the negation of the amplitude time series.

        Returns:
            CircAmpTimeSeries: The negation of the `CircAmpTimeSeries` object.
        """
        cats = CircAmpTimeSeries({}, self.backend)
        for channel, amp_time_series in cats.items():
            cats[channel] = -amp_time_series
        return cats

    def __pos__(self):
        """
        Returns a deep copy of the `CircAmpTimeSeries` object.

        Returns:
            CircAmpTimeSeries: A deep copy of the `CircAmpTimeSeries` object.
        """
        cats = self.deepcopy()
        return cats

    def __abs__(self):
        """
        Calculates the absolute values of the amplitude time series.

        Returns:
            CircAmpTimeSeries: The `CircAmpTimeSeries` object with absolute values.
        """
        cats = CircAmpTimeSeries({}, self.backend)
        for channel, amp_time_series in cats.items():
            cats[channel] = np.abs(amp_time_series)
        return cats

    def __add__(self, b):
        """
        Adds two `CircAmpTimeSeries` objects or a `CircAmpTimeSeries` object and a dictionary.

        Args:
            b (Union[CircAmpTimeSeries, dict]): The object to be added.

        Returns:
            CircAmpTimeSeries: The sum of the two objects.
        """
        if not isinstance(b, (CircAmpTimeSeries, dict)):
            raise ValueError("Input should be 'CircAmpTimeSeries' or 'dict'")
        if isinstance(b, CircAmpTimeSeries) and self.backend.configuration().backend_name != b.backend.configuration().backend_name:
            raise ValueError("Backend of the input must have the same backend")
        
        cats = CircAmpTimeSeries({}, self.backend)
        for channel, amp_time_series in b.items():
            channel = channel_rep(channel, use_channel=cats.use_channel)
            if channel not in cats.keys():
                cats[channel] = amp_time_series
            else:
                len_a = len(self[channel])
                len_b = len(b[channel])
                if len_a < len_b:
                    cats[channel] = np.concatenate((self[channel], np.zeros(len_b - len_a))) + b[channel]
                else:
                    cats[channel] = self[channel] + np.concatenate((b[channel], np.zeros(len_a - len_b)))
        
        cats.pad()
        
        return cats

    def __sub__(self, b):
        """
        Subtracts two `CircAmpTimeSeries` objects or a `CircAmpTimeSeries` object and a dictionary.

        Args:
            b (Union[CircAmpTimeSeries, dict]): The object to be subtracted.

        Returns:
            CircAmpTimeSeries: The result of the subtraction.
        """
        return self.__add__(-b)

    def __iadd__(self, b):
        """
        Adds a `CircAmpTimeSeries` object or a dictionary to the current object in place.

        Args:
            b (Union[CircAmpTimeSeries, dict]): The object to be added.

        Returns:
            CircAmpTimeSeries: The updated `CircAmpTimeSeries` object.
        """
        if not isinstance(b, (CircAmpTimeSeries, dict)):
            raise ValueError("Input should be 'CircAmpTimeSeries' or 'dict'")
        if isinstance(b, CircAmpTimeSeries) and self.backend.configuration().backend_name != b.backend.configuration().backend_name:
            raise ValueError("Backend of the input must have the same backend")
        
        for channel, amp_time_series in b.items():
            channel = channel_rep(channel, use_channel=self.use_channel)
            if channel not in self.keys():
                self[channel] = amp_time_series
            else:
                len_a = len(self[channel])
                len_b = len(b[channel])
                if len_a < len_b:
                    self[channel] = np.concatenate((self[channel], np.zeros(len_b - len_a))) + b[channel]
                else:
                    self[channel] = self[channel] + np.concatenate((b[channel], np.zeros(len_a - len_b)))
        
        self._amp_time_series_dict = CircAmpTimeSeries.pad_amp_time_series_dict(self._amp_time_series_dict)
        return self

    def __isub__(self, b):
        """
        Subtracts a `CircAmpTimeSeries` object or a dictionary from the current object in place.

        Args:
            b (Union[CircAmpTimeSeries, dict]): The object to be subtracted.

        Returns:
            CircAmpTimeSeries: The updated `CircAmpTimeSeries` object.
        """
        if isinstance(b, dict):
            for channel, amp_time_series in b.items():
                channel = channel_rep(channel, use_channel=self.use_channel)
                if channel not in self.keys():
                    self[channel] = amp_time_series
                else:
                    len_a = len(self[channel])
                    len_b = len(b[channel])
                    if len_a < len_b:
                        self[channel] = -np.concatenate((self, np.zeros(len_b - len_a))) + b[channel]
                    else:
                        self[channel] -= np.concatenate((b[channel], np.zeros(len_a - len_b)))
        else:
            self.__iadd__(-b)
        return self
