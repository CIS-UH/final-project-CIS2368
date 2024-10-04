import mysql.connector
from mysql.connector import Error 

def create_connection(host_name, user_name, user_password, db_name):
    connection = None 
    try: 
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name

        )
        print("connection sucessful")
    except Error as e: 
        print(f"the error '{e}' occured")
    return connection
