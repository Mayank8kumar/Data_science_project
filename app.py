# from src.Data_science import logger
from src.Data_science.logger import logging
from src.Data_science.exceptions import CustomerException 
from src.Data_science.components.data_ingestion import DataIngestion
from src.Data_science.components.data_ingestion import DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("the Execution has started")


    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomerException(e,sys)