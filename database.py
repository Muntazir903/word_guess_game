from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

local_session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()