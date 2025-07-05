import mysql.connector

try:
    
# Database connection details (replace with your own)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Levites123"
)

    mycursor = mydb.cursor()

# Create a table named `customers` (if it doesn't exist)
    mycursor.execute("""CREATE DATABASE IF NOT EXISTS alx_book_store;""")
 
except mysql.connector.Error as err:
    if err.errno == 1007:  # Database already exists error code
        print(f"Database '{database_name}' already exists. No need to create.")
    else:
        print(f"Error creating database: {err}")

mycursor.close()
mydb.close()
