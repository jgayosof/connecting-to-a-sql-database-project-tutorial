import psycopg2

conn = psycopg2.connect(database="", user="", password="", host="", port=5432)

cursor = conn.cursor()
cursor.execute("CREATE TABLE Persons(id INT PRIMARY KEY, name VARCHAR(20), age INT);")

conn.commit()
conn.close()