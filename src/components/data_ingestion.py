import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass 
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'modular_data', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'modular_data', 'test.csv')
    raw_data_path: str = os.path.join('data', 'raw.csv')

class DataIngestion: 
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        '''
        read the raw data and split the data train and test; save sets in modular_data inside artifacts folder
        
        :return train_set_filepath: file path of the training set
        :return test_set_filepath: file path of the testing set

        '''

        logging.info("method called initiate_data_ingestion")
        try:
            logging.info("reading raw data using pandas")
            df = pd.read_csv(self.ingestion_config.raw_data_path)

            #split the data
            logging.info("spliting the dataset into train and test")
            train_set, test_set = train_test_split(df, test_size=0.15, stratify=df["churn"], random_state=42)

            #if not exist make directory before saving 
            logging.info("creating required directory if doesn't exists")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            #save the sets
            logging.info("saving the train and test sets")
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("ingestion completed")
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

