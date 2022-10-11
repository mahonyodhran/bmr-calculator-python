
"""Module to connect to database
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

my_sql_conn = create_engine(
    "mysql://" + os.environ['DB_USER'] + ":" + os.environ['DB_PWD'] + "@" + os.environ['DB_HOST'] + ":" + str(os.environ['DB_PORT']) + "/" + os.environ['DB_BMR']
)

Session = sessionmaker(bind=my_sql_conn)
Base = declarative_base()