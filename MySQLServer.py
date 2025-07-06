import mysql.connector

try:
    conn = mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "JaphD@547169",
    )

    if conn.is_connected():
        mycursor = conn.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        mycursor.execute("USE alx_book_store")
        print("Database ready.")
        mycursor.close()
        conn.close()
    else:
        print("Failed to connect to MYSQL server.")

except mysql.connector.Error as e:
    print(f"Error while connecting to MYSQL: {e}")

    

