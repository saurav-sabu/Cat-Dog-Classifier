import os
import urllib.request as request
import requests
from zipfile import ZipFile, is_zipfile
from src.Dog_Cat_Classifier.entity import DataIngestionConfig
from src.Dog_Cat_Classifier import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            # Check if the file already exists
            logger.info(f"Checking if {self.config.local_data_file} already exists...")
            if not os.path.exists(self.config.local_data_file):
                print(f"Downloading file from {self.config.source_URL}...")

                # Check content type before downloading
                response = requests.head(self.config.source_URL)
                content_type = response.headers.get('Content-Type', '')

                # Stream the download to handle large files
                logger.info(f"Downloading file from {self.config.source_URL}...")
                with requests.get(self.config.source_URL, stream=True) as response:
                    response.raise_for_status()  # Raise an error for a bad status code
                    
                    # Open the destination file in binary write mode
                    with open(self.config.local_data_file, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):  # Read in 8KB chunks
                            f.write(chunk)

                print(f"File downloaded successfully: {self.config.local_data_file}")
            else:
                print("File already exists. Skipping download.")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")
            raise

    def _get_updated_list_of_files(self, list_of_files):
        # Filter the list of files to include only .jpg files that contain 'Cat' or 'Dog' in their names
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]
    
    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        # Define the target file path
        target_filepath = os.path.join(working_dir, f)
        
        # Extract the file if it does not already exist
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        
        # Remove the file if it is empty
        if os.path.getsize(target_filepath) == 0:
            os.remove(target_filepath)

    def unzip_and_clean(self):
        # Check if the local data file is a valid ZIP file
        logger.info(f"Checking if {self.config.local_data_file} is a valid ZIP file...")
        if not is_zipfile(self.config.local_data_file):
            raise ValueError(f"The file {self.config.local_data_file} is not a valid ZIP file.")
        
        # Open the ZIP file and process its contents
        logger.info(f"Unzipping and cleaning files from {self.config.local_data_file}...")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in updated_list_of_files:
                self._preprocess(zf, f, self.config.unzip_dir)