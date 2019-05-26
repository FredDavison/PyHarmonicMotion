
import pkg_resources
from configparser import ConfigParser

settings_path = pkg_resources.resource_filename('pymech', 'settings.conf')
global_settings = ConfigParser()
global_settings.read(settings_path)
