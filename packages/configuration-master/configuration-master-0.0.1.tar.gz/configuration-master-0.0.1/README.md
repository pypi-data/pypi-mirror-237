# config-master

**config-master** is a Python package designed for easy configuration management. It offers flexibility in storing and retrieving configuration data through global variables or environment variables.

## Installation

You can install **config-master** via pip:

```sh
pip install config-master
```

## Basic Usage

```python
from config_master import ConfigMaster

# Set a configuration value
ConfigMaster.set_config("my_key", "my_value")

# Get a configuration value
value = ConfigMaster.get_config_value("my_key")
print(value)
```

## Configuration Methods

You can manage your configuration in one of two ways based on your coding style.

1. **Using Environment Variables**
   By default, configuration values are stored as environment variables. This is recommended for security and encapsulation.
   ```python
   ConfigMaster.set_config("my_key", "my_value")
   ```

2. **Using Global Variables**
   If you prefer to manage configuration values using global variables, set the `use_global` parameter to True. Note that with global variables, you can only access them using the `ConfigMaster.get_config_value()` method.
   ```python
   ConfigMaster.use_global = True
   ConfigMaster.set_config("my_key", "my_value")
   ```

## Working with JSON Files

You can load configuration data from a JSON file:

```python
# Set configuration from a JSON file
ConfigMaster.set_config_from_json_file("config.json")
```

## Working with Dictionaries

Set multiple configuration values using a dictionary. The keys in the dictionary should match the variable names you intend to set.

```python
data = {
    "my_key": "my_value",
    "another_key": "another_value"
}

ConfigMaster.set_config_from_dict(data)

# Get a configuration value
value = ConfigMaster.get_config_value("my_key")
print(value)
```

**config-master** makes configuration management in Python a breeze, allowing you to choose the approach that best fits your project's needs.
