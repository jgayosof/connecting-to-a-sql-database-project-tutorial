# imports:
import os
import json
import psycopg2
import pandas as pd
import numpy as np
#from dbmodule import connect
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# load the .env file variables
load_dotenv()

# DB Connection variables:
host = str(os.getenv('Host'))
port = str(os.getenv('Port'))
dbname = str(os.getenv('Database'))
user_id = str(os.getenv('User'))
password = str(os.getenv('Password'))
uri = str(os.getenv('URI'))


# 1) Connect to the database here using the SQLAlchemy's create_engine function
def connect():
    # this allows us to use a global variable called engine:
    global engine 
    # A "connection string" is basically a string that contains all the databse credentials together
    connection_string = f'postgresql+psycopg2://'+user_id+':'+password+'@'+host+'/'+dbname
    print("Starting the connection...")
    engine = create_engine(connection_string)
    engine.connect()
    return engine

try:
    connect()
    print(f'Connection to the {host} for user {user_id} created successfully.')
except Exception as ex:
   print('Connection could not be made due to the following error: \n', ex)


# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
def execute_from_sql_file(file):
    file = open(f'src/sql/{file}')
    read_file = file.read()
    file.close()
    transactions = read_file.split(";")
    for transaction in transactions:
        try:
            engine.execute(transaction)
        except:
            continue

execute_from_sql_file("create.sql")

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
execute_from_sql_file("insert.sql")


# 4) Use pandas to print one of the tables as dataframes using read_sql function
df_publishers = pd.read_sql("Select * from publishers;", connect())
df_authors = pd.read_sql("Select * from authors;", engine)
df_books= pd.read_sql("Select * from books;", engine)
df_book_authors= pd.read_sql("Select * from book_authors;", engine)
print()
print("PUBLISHERS:")
print(df_publishers)
print()
print("AUTHORS:")
print(df_authors)
print()
print("BOOKS:")
print(df_books)
print()
print("BOOK AUTHORS:")
print(df_book_authors)