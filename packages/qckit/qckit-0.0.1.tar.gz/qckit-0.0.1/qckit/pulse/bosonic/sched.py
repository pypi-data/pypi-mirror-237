from typing import Iterable



class Sched:
    """
    Class for managing gate data and pulse schedules for a backend.
    """

    def __init__(self, backend):
        """
        Initializes the scheduler with the specified backend.

        Args:
            backend: Backend object.
        """
        self.backend = backend

        # example:
        # gate_data = [
        #     {
        #         "name": 'parametric_pulse',
        #         "label": 'pi_1_2',
        #         "pulse_shape": 'gaussian',
        #         "freq": None,
        #         'qubit': 0,
        #         "parameters": {
        #                         'duration': 160,
        #                         'amp': 0.15,
        #                         'sigma': 40,
        #                         'name': 'pi_1_2_pulse'
        #                     }
        #     }
        # ]
        self.gate_data = []

        self.scheds = []

        self.num_qubits = backend.configuration().num_qubits



    def add_gate_data(self, data_name, data):
        """
        Adds gate data to the scheduler.

        Args:
            data_name (str): Name of the gate data.
            data (dict): Dictionary containing gate parameters.
        """
        self.gate_data[data_name] = data



    def get_gate_data(self, data_name=None):
        """
        Retrieves gate data based on the provided data name.

        Args:
            data_name (str, optional): Name of the gate data to retrieve. Defaults to None.

        Returns:
            dict: Gate data dictionary.
        """
        if data_name:
            return self.gate_data[data_name]
        else:
            return self.gate_data



    def create_scheds(self):
        """
        Creates pulse schedules based on the stored gate data.
        """
        from qiskit import pulse
        for gate in self.gate_data:
            sched_dict = {
                "name": gate["name"],
                "label": gate["label"],
                "qubit": gate["qubit"]
            }
            with pulse.build(backend=self.backend, default_alignment='sequential', name=gate["label"]) as sched:
                drive_chan = pulse.drive_channel(gate["qubit"])
                if gate["freq"]:
                    pulse.set_frequency(gate["freq"], drive_chan)
                if gate["pulse_shape"] == 'gaussian':
                    waveform = pulse.Gaussian
                # TODO: add other waveform
                pulse.play(waveform(**gate["parameters"]), drive_chan)
            sched_dict["sched"] = sched
            self.scheds.append(sched_dict)



    def get_sched(self, label=None, qubit=None):
        """
        Retrieves a pulse schedule based on the provided label and qubit.

        Args:
            label (str, optional): Label of the pulse schedule to retrieve. Defaults to None.
            qubit (int or Iterable, optional): Qubit index or list of qubit indices. Defaults to None.

        Returns:
            pulse.Schedule or List[pulse.Schedule]: Retrieved pulse schedule(s).
        Raises:
            Exception: If the requested schedule is not found.
        """
        if isinstance(qubit, Iterable):
            sched_list = []
            for sched in self.scheds:
                if sched['label'] == label and sched['qubit'] in qubit:
                    sched_list.append(sched['sched'])
            if not sched_list:
                raise Exception("Schedule not found!")
            return sched_list
        elif isinstance(qubit, int):
            for sched in self.scheds:
                if sched['label'] == label and sched['qubit'] == qubit:
                    return sched['sched']
            raise Exception("Schedule not found!")



    def get_scheds(self):
        """
        Retrieves all stored pulse schedules.

        Returns:
            List[pulse.Schedule]: List of pulse schedules.
        """
        return self.scheds



    def save_gate_data(self, filename=None):
        """
        Saves gate data to a JSON file.

        Args:
            filename (str, optional): File path to save the gate data. Defaults to None.
        """
        import json, os, sys
        with open(filename if filename else os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), self.backend.name() + "_gate_data.json"), "w") as f:
            json.dump(self.gate_data, f, indent = 4)


    
    def load_gate_data(self, filename=None):
        """
        Loads gate data from a JSON file and creates pulse schedules.

        Args:
            filename (str, optional): File path to load the gate data. Defaults to None.

        Returns:
            dict: Loaded gate data.
        """
        import json, os, sys
        with open(filename if filename else os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), self.backend.name() + "_gate_data.json"), "r") as f:
            self.gate_data = json.load(f)
        self.create_scheds()
        return self.gate_data



    def parse_pi_12_23_gate_data(self, freq_12_list, pi_amp_12_list, freq_23_list, pi_amp_23_list, pi_duration_12=160, pi_sigma_12=40, pi_duration_23=160, pi_sigma_23=40, save=False, filename=None):
        """
        Parses gate data for pi pulses on qubits 1->2 and 2->3 and creates pulse schedules.

        Args:
            freq_12_list (Iterable): Frequency list for qubits 1->2.
            pi_amp_12_list (Iterable): Pi pulse amplitudes for qubits 1->2.
            freq_23_list (Iterable): Frequency list for qubits 2->3.
            pi_amp_23_list (Iterable): Pi pulse amplitudes for qubits 2->3.
            pi_duration_12 (int, optional): Duration of pi pulse on qubits 1->2. Defaults to 160.
            pi_sigma_12 (int, optional): Sigma parameter of the Gaussian pulse on qubits 1->2. Defaults to 40.
            pi_duration_23 (int, optional): Duration of pi pulse on qubits 2->3. Defaults to 160.
            pi_sigma_23 (int, optional): Sigma parameter of the Gaussian pulse on qubits 2->3. Defaults to 40.
            save (bool, optional): Whether to save the gate data to a file. Defaults to False.
            filename (str, optional): File path to save the gate data. Defaults to None.
        """
        for qubit, (freq, amp) in enumerate(zip(freq_12_list, pi_amp_12_list)):
            self.gate_data.append({
                    "name": 'parametric_pulse',
                    "label": 'pi_1_2',
                    "pulse_shape": 'gaussian',
                    "freq": freq,
                    'qubit': qubit,
                    "parameters": {
                                    'duration': pi_duration_12,
                                    'amp': amp,
                                    'sigma': pi_sigma_12,
                                    'name': 'pi_1_2_pulse'
                                }
            })

        for qubit, (freq, amp) in enumerate(zip(freq_23_list, pi_amp_23_list)):
            self.gate_data.append({
                    "name": 'parametric_pulse',
                    "label": 'pi_2_3',
                    "pulse_shape": 'gaussian',
                    "freq": freq,
                    'qubit': qubit,
                    "parameters": {
                                    'duration': pi_duration_23,
                                    'amp': amp,
                                    'sigma': pi_sigma_23,
                                    'name': 'pi_2_3_pulse'
                                }
            })
        
        if save:
            self.save_gate_data(filename)
