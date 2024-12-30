import os
from box.exceptions import BoxValueError
import yaml
from src.Dog_Cat_Classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(file_path: str) -> ConfigBox:
    """
    Read a yaml file and return the content as a dictionary
    """
    try:
        with open(file_path, "r") as file:
            content = yaml.safe_load(file)
            logger.info(f"Read the yaml file: {file_path}")
            return ConfigBox(content)
    except BoxValueError:
            raise ValueError(f"Error reading the yaml file: {file_path}")
    except Exception as e:
            raise e
    
@ensure_annotations
def create_directory(path_to_directory: list):
    """
    Create a directory if it does not exist
    """
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Created directory: {path}")


@ensure_annotations
def save_json(file_path: str, data: dict):
    """
    Save a dictionary as a json file
    """
    with open(file_path, "w") as file:
        json.dump(data, file,indent=4)
        logger.info(f"Saved the json file: {file_path}")

@ensure_annotations
def load_json(file_path: str) -> ConfigBox:
    """
    Load a json file as a dictionary
    """
    with open(file_path, "r") as file:
        data = json.load(file)
        logger.info(f"Loaded the json file: {file_path}")
    
    return ConfigBox(data)

@ensure_annotations
def save_model(model, file_path: str):
    """
    Save a model using joblib
    """
    joblib.dump(model, file_path)
    logger.info(f"Saved the model: {file_path}")

@ensure_annotations
def load_model(file_path: str) -> Any:
    """
    Load a model using joblib
    """
    model = joblib.load(file_path)
    logger.info(f"Loaded the model: {file_path}")
    return model

def get_size(file_path: str) -> str:
    """
    Get the size of a file
    """
    size = round(os.path.getsize(file_path)/1024)
    logger.info(f"Size of the file: {file_path} is {size} KB")
    return size