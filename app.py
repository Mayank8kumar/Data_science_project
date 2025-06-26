# from src.Data_science import logger
from src.Data_science.logger import logging
from src.Data_science.exceptions import CustomerException 
import sys

if __name__=="__main__":
    logging.info("the Execution has started")


    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomerException(e,sys)