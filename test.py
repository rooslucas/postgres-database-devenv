import numpy as np
import pandas as pd
import psycopg2

print("hello world")

print(np.add(3,4))

try:
    connection = psycopg2.connect(
        dbname="mydb",
        user="postgres",
        password="testing",
        host="localhost"
    )

    cursor = connection.cursor()
    
except Exception as e:
    print(f"An error occurred: {e}")

dbname = 'funsies'
# cursor.execute("CREATE TABLE funsies (ID INT PRIMARY KEY, ITEM TEXT, FUN_FACTOR INT)")
# cursor.execute("INSERT INTO funsies (ID, ITEM, FUN_FACTOR) VALUES (1, 'rollerblade', 8 )")
# cursor.execute("INSERT INTO funsies (ID, ITEM, FUN_FACTOR) VALUES (2, 'skate', 4 )")

# connection.commit()

cursor.execute(f"SELECT * FROM {dbname}")

print(cursor.fetchall())