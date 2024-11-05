import numpy as np
import mysql.connector

print("hello world")

print(np.add(3,4))

c = mysql.connector.connect(host="localhost",
  user="yourusername",
  password="yourpassword"
)