

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.db.db_base import Base
from .models.log import Log

class LogsDBCreater():


    def __init__(self,db_path:str) -> None:
        self.db_path = db_path
        self.session = None
        

    def create_session(self):
        engine = create_engine(self.db_path)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def create(self,log:Log):
        if self.session == None:
            raise Exception("session not exsist")
        
        self.session.add(log)
        self.session.commit()
    