import os

from dotenv import load_dotenv
load_dotenv()  

from src import DSLoader
from src import LogsDBCreater

if __name__ == "__main__":

    logs = LogsDBCreater(os.getenv("LOGS_PATH"))
    logs.create_session()
    logs.create()



    # loader = DSLoader(os.getenv("DATASET_TRANSLATOR"),100)

    # for line in loader.readDataset():
    #     print(line)    

