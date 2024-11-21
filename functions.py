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

def create_list(list_name: str):
    connection, cursor = connect()
    try:
        cursor.execute(f"CREATE TABLE {list_name} (ID INT PRIMARY KEY, ITEM TEXT)")
    
    except:
        print("This list was already created")
    
    connection.commit()
    connection.close()

    print("List Created")

def add_item(db, id, item):
    connection, cursor = connect()   

    try:  
        cursor.execute(f"INSERT INTO {db} (ID, ITEM) VALUES ({id}, {item})")
    except:
        print(f"This item was already added")
    
    connection.commit()
    connection.close()

    print("Added")

def remove_item(db, id):
    connection, cursor = connect()

    try:  
        cursor.execute(f"DELETE FROM {db} WHERE ID={id}")
    except:
        print(f"This item was already removed")

    connection.commit()
    connection.close()

    print("Removed")

def view(db):
    connection, cursor = connect()

    cursor.execute(f"SELECT * FROM {db}")
        
    connection.commit()
    connection.close()

    print("View")

