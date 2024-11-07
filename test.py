import numpy as np
import pandas as pd
import psycopg2

print("hello world")

print(np.add(3,4))

try:
    connection = psycopg2.connect(
        dbname="mydb",
        user="rose",
        host="localhost"
    )

    cursor = connection.cursor()
    
except Exception as e:
    print(f"An error occurred: {e}")