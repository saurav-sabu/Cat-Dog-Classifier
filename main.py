from src.Dog_Cat_Classifier.pipeline.stage_01_pipeline import Data_Ingestion_Training_pipeline
from src.Dog_Cat_Classifier import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"--------{STAGE_NAME} started-----------")
    data_ingestion = Data_Ingestion_Training_pipeline()
    data_ingestion.main()
    logger.info(f"--------{STAGE_NAME} completed-----------")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e
