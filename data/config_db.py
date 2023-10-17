import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('HOST')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')

engine = create_engine(f"postgresql+psycopg2://postgres:{password}@{host}/{database}", echo=True)
metadata = MetaData()

Base = declarative_base()