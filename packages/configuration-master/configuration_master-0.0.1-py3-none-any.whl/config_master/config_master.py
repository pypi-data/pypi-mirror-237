import json
import os
from typing import Dict, Any, Union

from config_master.exceptions import LoadJsonFileException, ConfigException


class ConfigMaster:
    """
    A class for managing configuration settings.

    Attributes:
        use_global (bool): A flag indicating whether to use global variables or environment variables.
    """

    use_global = False

    @staticmethod
    def read_json_file(file_path: str) -> Dict:
        """
        Reads a JSON file and returns its contents as a dictionary.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The contents of the JSON file as a dictionary.

        Raises:
            LoadJsonFileException: If there was an error loading or decoding the JSON file.
            ConfigException: If unhandled exception occurs
        """
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except IOError as e:
            raise LoadJsonFileException(f"Error loading JSON file: {e}")
        except json.JSONDecodeError as e:
            raise LoadJsonFileException(f"Error decoding JSON file: {e}")
        except Exception as e:
            raise ConfigException(f"Error while loading Json file: {e}")

    @staticmethod
    def set_config(key: str, value: Any):
        """
        Sets a configuration value.

        Args:
            key (str): The key of the configuration value.
            value (Any): The value of the configuration value.

        Raises:
            ConfigException: If there was an error setting the configuration value.
        """
        try:
            if ConfigMaster.use_global:
                globals()[key] = value
            elif isinstance(value, str):
                os.environ[key] = value
            elif type(value) in [int, bool, float]:
                os.environ[key] = str(value)
            else:
                os.environ[key] = json.dumps(value)
        except Exception as e:
            raise ConfigException(f"Error setting key-value pair: {e}")

    @staticmethod
    def set_config_from_dict(data: Dict):
        """
        Sets configuration values from a dictionary.

        Args:
            data (dict): The dictionary containing the configuration values.

        Raises:
            ConfigException: If there was an error setting the configuration values.
        """
        try:
            for key, value in data.items():
                ConfigMaster.set_config(key=key, value=value)
        except Exception as e:
            raise ConfigException(f"Error setting dictionary: {e}")

    @staticmethod
    def set_config_from_json_file(file_path: str):
        """
        Sets configuration values from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Raises:
            ConfigException: If there was an error setting the configuration values.
        """
        try:
            data = ConfigMaster.read_json_file(file_path=file_path)
            ConfigMaster.set_config_from_dict(data=data)
        except Exception as e:
            raise ConfigException(f"Error setting from JSON file: {e}")

    @staticmethod
    def get_config_value(key: str) -> Any:
        """
        Gets the value of a configuration setting.

        Args:
            key (str): The key of the configuration setting.

        Returns:
            Union[str, Any]: The value of the configuration setting.

        Raises:
            ConfigException: If the configuration setting does not exist.
        """
        try:
            return globals()[key] if ConfigMaster.use_global else os.environ[key]
        except Exception as e:
            raise ConfigException(f"Error getting key-value pair: {e}")
