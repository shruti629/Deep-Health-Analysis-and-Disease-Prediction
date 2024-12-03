import os
import sys
from src.logger import logging
from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

##intitialize the data ingestion configuration

@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

#create the data ingestion class
class   DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig() 

    def initiate_data_ingestion(self):
      logging.info('Data Ingestion method starts')

      try:
        # Read the dataset
          df = pd.read_csv(os.path.join('notebooks/data', 'heart.csv'))
          logging.info('Dataset read as pandas DataFrame')

        # Ensure directory exists
          raw_dir = os.path.dirname(self.ingestion_config.raw_data_path)
          os.makedirs(raw_dir, exist_ok=True)

        # Remove existing file if it exists
          if os.path.exists(self.ingestion_config.raw_data_path):
            os.remove(self.ingestion_config.raw_data_path)

        # Save raw data
          df.to_csv(self.ingestion_config.raw_data_path, index=False)
          logging.info(f'Raw data saved at {self.ingestion_config.raw_data_path}')

        # Train-test split
          train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

        # Save train data
          if os.path.exists(self.ingestion_config.train_data_path):
            os.remove(self.ingestion_config.train_data_path)
          train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

        # Save test data
          if os.path.exists(self.ingestion_config.test_data_path):
            os.remove(self.ingestion_config.test_data_path)
          test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

          logging.info('Train-test split completed and data saved')

        # Return paths
          return (
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path
        )

      except Exception as e:
        logging.error('Exception occurred at Data Ingestion Stage')
        raise CustomException(e, sys)


