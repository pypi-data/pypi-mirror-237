import argparse, os, json

class Settings:
    """
    A class for managing settings for the benchmarking tool.

    Attributes:
        settings_path (str): The path to the settings file.
        settings_data (dict): A dictionary containing the settings data.
    """
    def __init__(self, settings_path = None):
        """
        Initializes a Settings object.

        Args:
            settings_path (str): The path to the settings file. If None, the default path is used.
        """
        if not settings_path:
            settings_path = os.path.join(os.path.dirname(__file__), "settings.json")
        self.settings_path = settings_path
        self.settings_data = self.load_settings(settings_path)

    @staticmethod
    def load_settings(settings_path = None):
        """
        Loads the settings data from a JSON file.

        Args:
            settings_path (str): The path to the settings file. If None, the default path is used.

        Returns:
            dict: A dictionary containing the settings data.
        """
        if not settings_path:
            settings_path = os.path.join(os.path.dirname(__file__), "settings.json")
        
        if os.path.exists(settings_path):
            with open(settings_path, "r") as f:
                settings_data = json.load(f)
        else:
            settings_data = {}
            settings_data["benchmark_paths"] = {}
            settings_data["notifier"] = {}
        
        return settings_data

    def save_settings(self):
        """
        Saves the settings data to the settings file.
        """
        with open(self.settings_path, "w") as f:
            json.dump(self.settings_data, f, indent = 4)

    def set_path_qasmbench(self, path):
        """
        Sets the path to the QASM benchmark directory.

        Args:
            path (str): The path to the QASM benchmark directory.
        """
        self.settings_data["benchmark_paths"]["qasmbench"] = path
        self.save_settings()
    
    @property
    def path_qasmbench(self):
        """
        Returns:
            str: The path to the QASM benchmark directory.
        """
        return self.settings_data["benchmark_paths"]["qasmbench"]

    def set_notifier(self, from_addr, password, to_addr, smtp_host, smtp_port):
        self.settings_data["notifier"]["from_addr"] = from_addr
        self.settings_data["notifier"]["password"] = password
        self.settings_data["notifier"]["to_addr"] = to_addr
        self.settings_data["notifier"]["smtp_host"] = smtp_host
        self.settings_data["notifier"]["smtp_port"] = smtp_port
        self.save_settings()
    
    @property
    def notifier_from_addr(self):
        return self.settings_data["notifier"]["from_addr"]
    
    @property
    def notifier_password(self):
        return self.settings_data["notifier"]["password"]
    
    @property
    def notifier_to_addr(self):
        return self.settings_data["notifier"]["to_addr"]
    
    @property
    def notifier_smtp_host(self):
        return self.settings_data["notifier"]["smtp_host"]
    
    @property
    def notifier_smtp_port(self):
        return self.settings_data["notifier"]["smtp_port"]



def configure():
    """
    Configures the benchmarking tool using command-line arguments.

    Command-line arguments:
        --qasmbench (str): The path to the QASMBench directory.

    Example usage:
        python configure.py --qasmbench /path/to/qasmbench
    """
    parser = argparse.ArgumentParser("configure")
    parser.add_argument("--qasmbench", help = "Set the path to QASMBench", type = str)
    args = parser.parse_args()

    settings = Settings()

    settings.set_path_qasmbench(args.qasmbench)

if __name__ == "__main__":
    configure()
    