import mysql.connector

def connect_to_mysql():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host="localhost",      # MySQL server hostname
            user="root",           # Replace with your username
            password="123456789",  # Replace with your password
            database="learn_english",  # Replace with your database name
            port=3306              # Default MySQL port
        )
        print("Connection to MySQL established successfully!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def fetch_data_from_table(connection):
    try:
        # Create a cursor object
        cursor = connection.cursor()
        
        # Define the SQL query to fetch data
        fetch_query = "SELECT * FROM word_meaning;"
        
        # Execute the query
        cursor.execute(fetch_query)
        
        # Fetch all rows from the executed query
        results = cursor.fetchall()
        
        # Display the fetched data
        print("Data from 'word_meaning' table:")
        for row in results:
            print(row)  # Each row is a tuple (e.g., (1, 'A-एक'))
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor
        cursor.close()

if __name__ == "__main__":
    # Connect to the database
    connection = connect_to_mysql()
    
    if connection:
        # Fetch data from the table
        fetch_data_from_table(connection)
        
        # Close the connection
        connection.close()
        print("Connection closed!")
