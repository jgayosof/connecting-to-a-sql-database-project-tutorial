# imports:
import os
import json
import psycopg
import pandas as pd
#from dbmodule import connect
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# load the .env file variables
load_dotenv()

# DB Connection variables:
host = os.getenv('Host')
port = os.getenv('Port')
dbname = os.getenv('Database')
user_id = os.getenv('User')
password = os.getenv('Password')
uri = os.getenv('URI')
uri = 'postgresql://jzrkqkkrursbhk:b600423acf502961236ca041ffb988656125673c2b35e3438ea465bf34c51eb5@decano.com:5432/d98brgoqiv39mu'


# 1) Connect to the database here using the SQLAlchemy's create_engine function
'''
connection = psycopg.connect(dbname=dbname, host=host, port = port, user=user_id, password=password)
cursor = connection.cursor()
'''

def connect(connection_string):
    # this allows us to use a global variable called engine:
    global engine 
    # A "connection string" is basically a string that contains all the databse credentials together
    ## connection_string = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
    #connection_string = 'postgresql+psycopg2://'+user_id+':'+password+'@'+host+'/'+dbname
    #connection_string = URI
    print(connection_string)
    print("Starting the connection...")
    engine = create_engine(connection_string)
    engine.connect()
    return engine

try:
    ##connection = create_engine('postgresql+psycopg2://'+user_id+':'+password+'@'+host+'/'+dbname)
    connect(uri)
    print(f'Connection to the {host} for user {user_id} created successfully.')
except Exception as ex:
   print('Connection could not be made due to the following error: \n', ex)

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function
