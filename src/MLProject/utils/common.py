import os
import yaml
from src.MLProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (str): The file path to the YAML file. Must be a string.
    Returns:
        ConfigBox: A ConfigBox object containing the contents of the YAML file.
    Raises:
        ValueError: If the provided path is not a string or if the file cannot be read.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully read YAML file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error converting YAML content to ConfigBox: {e}")
        raise
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise  e 
