import json


class DSLoader():

    def __init__(self,filePath:str,chunk_size:int) -> None:
        self.file_path = filePath
        self.chunk_size = chunk_size
        

    def readDataset(self):

        try:

            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)['rows']  
                
                for i in range(0, len(data), self.chunk_size):
                    yield data[i:i + self.chunk_size]

        except Exception as e :
            print(e)


    def setChunkSize(self,chunk_size:int):
        self.chunk_size = chunk_size
    
    def getChunkSize(self):
        return self.chunk_size
