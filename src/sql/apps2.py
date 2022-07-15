import pandas as pd
import numpy as np
import sqlalchemy as db
import os
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import *

load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# 1) Connect to the database here using the SQLAlchemy's create_engine function

def connect():
    global engine # this allows us to use a global variable called engine
    # A "connection string" is basically a string that contains all the databse credentials together
    connection_string = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    print("Starting the connection...")
    engine = create_engine(connection_string)
    engine.connect()
    return engine

connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

def execute_from_sql_file(file):
    file = open(f'sql/{file}')
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
df_publishers = pd.read_sql("Select * from publishers;", engine)
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