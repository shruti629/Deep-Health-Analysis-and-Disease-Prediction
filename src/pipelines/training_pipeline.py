#import os
#import sys
#from src.logger import logging
#from src.exception import CustomException
#import pandas as pd

#from src.components.data_ingestion import DataIngestion


#if __name__=='__main__':
    #obj=DataIngestion()
    #train_data_path,test_data_path=obj.initiate_data_ingestion()
    #print(train_data_path,test_data_path)

import os 
import sys 
from src.logger import logging 
from src.exception import CustomException 
class DataIngestion: 
    def __init__(self, ingestion_config): 
        self.ingestion_config = ingestion_config 
    def initiate_data_ingestion(self): 
        try: 
            if os.path.exists(self.ingestion_config.raw_data_path): 
                os.remove(self.ingestion_config.raw_data_path) 
        except PermissionError as e: 
            logging.error(f"Permission error: {e}") 
            raise CustomException(e, sys) 
        except Exception as e: 
          logging.error(f"An error occurred: {e}") 
          raise CustomException(e, sys)






    
