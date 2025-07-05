import mysql.connector

# Database connection details (replace with your own)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Levites123"
)

mycursor = mydb.cursor()

# Create a table named `customers` (if it doesn't exist)
mycursor.execute("""
CREATE DATABASE IF NOT EXISTS alx_book_store;""")

mycursor.close()
mydb.close()
