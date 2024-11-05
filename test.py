import numpy as np
import psycopg2

print("hello world")

print(np.add(3,4))

conn = psycopg2.connect(database = "datacamp_courses", 
                        user = "datacamp", 
                        host= 'localhost',
                        password = "postgresql_tutorial",
                        port = 5432)