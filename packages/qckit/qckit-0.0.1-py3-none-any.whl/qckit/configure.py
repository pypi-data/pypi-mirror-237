import os
from qcutils import Settings

_settings_path = os.path.join(os.path.dirname(__file__), "settings.json")
settings = Settings(_settings_path)

# set QASMbench
# qasmbench_path = 
# settings.set_path_qasmbench(qasmbench_path)

# set notifier
# from_addr =
# password = 
# to_addr = 
# smtp_host = 
# smtp_port = 

# settings.set_notifier(from_addr, password, to_addr, smtp_host, smtp_port)