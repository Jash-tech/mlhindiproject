from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion,DataIngestionConfig
import sys
import os


if __name__=="__main__":
    logging.info("Execution Started")


    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise CustomException(e,sys)