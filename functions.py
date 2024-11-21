import psycopg2

def connect():
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
    
    return connection, cursor

def create_list():
    connection, cursor = connect()
    print("List Created")

def add_item():
    connection, cursor = connect()
    print("Added")

def remove_item():
    connection, cursor = connect()
    print("Removed")

def view():
    connection, cursor = connect()
    print("View")

