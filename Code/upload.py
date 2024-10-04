import mysql.connector
from mysql.connector import Error


def connect_db():
    try:
        conn = mysql.connector.connect(
        host='your_host_name',
        database= 'aws rds database name',
        user= 'username',
        password= 'password'
    )

    except Error as e:
        print(f"Error: {e}")
    return conn 


        