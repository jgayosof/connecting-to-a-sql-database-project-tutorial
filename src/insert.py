import psycopg2

conn = psycopg2.connect(database="", user="", password="", host="", port=5432)

cursor = conn.cursor()
cursor.execute("INSERT INTO Persons(id, name, age) VALUES (1, 'Atilio', 59), (2, 'Abdon', 25), (3, Hugo, 64);")

conn.commit()
conn.close()