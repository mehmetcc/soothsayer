from configparser import ConfigParser

from .utils import FileUtils


class ConfigurationService:
    def __init__(self, config_file: str = "config.ini") -> None:
        self._config = ConfigParser()
        self._config.read(self._load_config(config_file))

    def load(self) -> ConfigParser:
        return self._config

    def _load_config(self, config_file: str) -> str:
        return FileUtils.get_caller_parent() + "/" + config_file
