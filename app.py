# from src.Data_science import logger
from src.Data_science.logger import logging
from src.Data_science.exceptions import CustomException 
from src.Data_science.components.data_ingestion import DataIngestion
from src.Data_science.components.data_ingestion import DataIngestionConfig
from src.Data_science.components.data_transformation import DataTransformationConfig, DataTransformation
import sys

if __name__=="__main__":
    logging.info("the Execution has started")

    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        logging.info("Data ingestion completed ")
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        # data_transformation_config= DataTransformationConfig()
        data_transformation= DataTransformation()
        logging.info("Data Tranformation completed ")
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(sys,e)