import os
from importlib import import_module

from aquilo.main import Aquilo
from aquilo.management.cli import *

settings = import_module(os.environ.get("AQUILO_SETTINGS_MODULE"))

app = Aquilo(debug=settings.DEBUG)
