import os
from configparser import ConfigParser


import ipdb; ipdb.set_trace()
assert os.path.exists('settings.conf')
global_settings = ConfigParser()
global_settings.read('settings.conf')
