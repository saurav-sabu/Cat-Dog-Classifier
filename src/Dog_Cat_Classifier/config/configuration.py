from src.Dog_Cat_Classifier.constants import *
from src.Dog_Cat_Classifier.utils import read_yaml, create_directory
from src.Dog_Cat_Classifier.entity import DataIngestionConfig

import os
from pathlib import Path


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = os.path.normpath(str(CONFIG_FILE_PATH)),
        params_filepath = os.path.normpath(str(PARAMS_FILE_PATH))):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directory([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
      