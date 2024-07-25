import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python',
                                         user='root',
                                         password='dbpass@123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor() # opening mysql command prompt 
        cursor.execute("select database();") # executing the mysql command "show databases; use python;"
        record = cursor.fetchone()   # reading the output from the memory 
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()  # closing the database connection 
        connection.close()  # closing the entire session to mysql connection
        print("MySQL connection is closed")