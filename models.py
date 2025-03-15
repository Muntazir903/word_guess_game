from sqlalchemy import Integer,String,Column
from database import Base

class Score(Base):
    __tablename__ = "scores"
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String, index=True)
    guessed_word = Column(String,index=True)
    score = Column(Integer)