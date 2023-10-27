import json
import os
from typing import Dict, Any
from unittest.mock import patch, mock_open, call

import pytest

from config_master.config_master import ConfigMaster, LoadJsonFileException
from config_master.exceptions import ConfigException


class TestConfigMaster:
    @pytest.fixture
    def data(self) -> Dict[str, Any]:
        return {"key1": "value1", "key2": 2}

    @pytest.fixture
    def config_master(self):
        return ConfigMaster()

    @pytest.fixture
    def json_data(self):
        return {"key1": "value1", "key2": "value2"}

    @pytest.fixture
    def json_file(self):
        return "test.json"

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='{"key1": "value1", "key2": "value2"}',
    )
    def test_read_json_file_success(
        self, mock_file, config_master, json_file, json_data
    ):
        # Arrange
        expected_output = json_data

        # Act
        with patch("json.load", return_value=json_data):
            output = config_master.read_json_file(json_file)

        # Assert
        assert output == expected_output
        mock_file.assert_called_once_with(json_file, "r")

    @patch("builtins.open", side_effect=IOError("File not found"))
    def test_read_json_file_file_not_found(self, mock_file, config_master, json_file):
        # Arrange
        expected_exception = LoadJsonFileException(
            "Error loading JSON file: File not found"
        )

        # Act & Assert
        with pytest.raises(LoadJsonFileException) as exc_info:
            config_master.read_json_file(json_file)
        assert str(exc_info.value) == str(expected_exception)
        mock_file.assert_called_once_with(json_file, "r")

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='{"key1": "value1", "key2": "value2"}',
    )
    @patch(
        "json.load", side_effect=json.JSONDecodeError("Expecting property name", "", 0)
    )
    def test_read_json_file_json_decode_error(
        self, mock_json, mock_file, config_master, json_file
    ):
        # Arrange
        expected_exception = LoadJsonFileException(
            "Error decoding JSON file: Expecting property name: line 1 column 1 (char 0)"
        )

        # Act & Assert
        with pytest.raises(LoadJsonFileException) as exc_info:
            config_master.read_json_file(json_file)
        assert str(exc_info.value) == str(expected_exception)
        mock_file.assert_called_once_with(json_file, "r")
        mock_json.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_read_json_file_empty_file(self, mock_file, config_master, json_file):
        # Arrange
        expected_output = {}

        # Act
        with patch("json.load", return_value={}):
            output = config_master.read_json_file(json_file)

        # Assert
        assert output == expected_output
        mock_file.assert_called_once_with(json_file, "r")

    @pytest.mark.parametrize(
        "key, value",
        [
            ("key1", "value1"),
            ("key2", "2"),
            ("key3", "value3"),
            ("key4", "4"),
        ],
    )
    def test_set_config_with_globals(
        self, config_master: ConfigMaster, key: str, value: Any
    ):
        # Arrange
        config_master.use_global = True

        # Act
        config_master.set_config(key, value)

        # Assert
        assert config_master.get_config_value(key) == value

    @pytest.mark.parametrize(
        "value, expected_result",
        [
            (1, "1"),
            (False, "False"),
            (True, "True"),
            (-1, "-1"),
            ("21", "21"),
            (1.05, "1.05"),
            (-1.05, "-1.05"),
        ],
    )
    def test_set_config_as_env_vars_with_primitive_datatype_value_returns_str_value(
        self, config_master: ConfigMaster, value, expected_result
    ):
        # Arrange
        key = "key1"
        with patch.object(ConfigMaster, "use_global", False):
            # Act
            config_master.set_config(key, value)
            # Assert
            assert os.environ[key] == expected_result

    @pytest.mark.parametrize(
        "value",
        [
            ({"key1": "val1", "key2": "val2"}),
            ([{"key1": "val1", "key2": "val2"}, {"key3": "val3", "key4": "val4"}]),
        ],
    )
    def test_set_config_as_env_vars_with_complex_datatype_value_returns_json_str(
        self, config_master: ConfigMaster, value, snapshot
    ):
        # Arrange
        key = "key1"
        with patch.object(ConfigMaster, "use_global", False):
            with patch.dict(os.environ, {key: str(value)}):
                # Act
                config_master.set_config(key, value)
                # Assert
                snapshot.assert_match(os.environ[key])

    def test_set_config_from_dict(
        self, config_master: ConfigMaster, data: Dict[str, Any]
    ):
        # Arrange
        with patch.object(ConfigMaster, "set_config") as set_config_mock:
            # Act
            config_master.set_config_from_dict(data)
            # Assert
            set_config_mock.assert_has_calls(
                [call(key="key1", value="value1"), call(key="key2", value=2)]
            )

    @patch.object(ConfigMaster, "read_json_file")
    def test_set_config_from_json_file(
        self,
        read_json_file_mock,
        config_master: ConfigMaster,
        json_file: str,
        data: Dict[str, Any],
    ):
        # Arrange
        read_json_file_mock.return_value = data

        with patch.object(ConfigMaster, "set_config_from_dict") as set_config_mock:
            # Act
            config_master.set_config_from_json_file(json_file)
            # Assert
            set_config_mock.assert_called_once_with(data=data)

    def test_set_config_from_json_file_with_exception(
        self, config_master: ConfigMaster, json_file: str
    ):
        # Arrange
        with patch.object(ConfigMaster, "set_config_from_dict", side_effect=Exception):
            # Act & Assert
            with pytest.raises(ConfigException):
                config_master.set_config_from_json_file(json_file)

    def test_get_config_value(self, config_master: ConfigMaster, data: Dict[str, Any]):
        # Arrange
        os.environ["key"] = "value"

        # Act
        result = config_master.get_config_value("key")

        # Assert
        assert result == "value"

    def test_get_config_value_with_globals(
        self, config_master: ConfigMaster, data: Dict[str, Any]
    ):
        # Arrange
        config_master.use_global = True
        config_master.set_config("key_1", "value_1")

        # Act
        result = config_master.get_config_value("key_1")

        # Assert
        assert result == "value_1"
