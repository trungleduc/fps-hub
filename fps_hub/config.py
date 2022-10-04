from fps.config import PluginModel
from fps.config import get_config as fps_get_config
from fps.hooks import register_config, register_plugin_name

class HubConfig(PluginModel):
    random: bool = False


def get_config():
    return fps_get_config(HubConfig)


c = register_config(HubConfig)
n = register_plugin_name("fps_hub")