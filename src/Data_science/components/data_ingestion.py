import os
import sys
from src.Data_science.exceptions import CustomException
from src.Data_science.logger import logging
import pandas as pd 
from src.Data_science.utils import read_sql_data
from sklearn.model_selection import train_test_split


from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # df=read_sql_data()
            df=pd.read_csv(os.path.join('artifacts','raw.csv'))   ## Not reading it again from the database. 
            logging.info("Reading from mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            # logging.info("Data Ingestion is completed part I")
            # print("**************************************************************")
            # print(df.head())
            # print("**************************************************************")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)