import os
from ._settings import Settings, configure
from .credential import *

_settings_path = os.path.join(os.path.dirname(__file__), "settings.json")
settings = Settings(_settings_path)
