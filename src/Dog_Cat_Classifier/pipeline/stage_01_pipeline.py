from src.Dog_Cat_Classifier.config import ConfigurationManager
from src.Dog_Cat_Classifier.components.data_ingestion import DataIngestion


class Data_Ingestion_Training_pipeline:

    def __init__(self):
        pass

    def main(self):
        try:
            # Initialize the ConfigurationManager
            config = ConfigurationManager()
            
            # Get the data ingestion configuration
            data_ingestion_config = config.get_data_ingestion_config()
            
            # Initialize the DataIngestion class with the configuration
            data_ingestion = DataIngestion(config=data_ingestion_config)
            
            # Download the data file
            data_ingestion.download_file()
            
            # Unzip and clean the downloaded data file
            data_ingestion.unzip_and_clean()
        except Exception as e:
            # Raise any exceptions that occur
            raise e