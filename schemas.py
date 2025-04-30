import pymysql

sqlpass = "Iondragonfly23!"  #Database password
inventory_name = "inventory_db" #Database name
   

def DatabaseSetup():
    
    # Connect to the MySQL database
    connection = pymysql.connect(
        host="localhost",               # Host where the database is located
        user="root",                    # Sets database username
        password=sqlpass,               # Sets password for the database
        database=inventory_name         # Sets Name of the database to connect to
    )

    cursor = connection.cursor()        # Creates a cursor object to execute SQL commands

    # Create the 'products' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(100) NOT NULL,
        quantity INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        category VARCHAR(50)
        )
    """)

    #Creates Miscellaneous Attribute table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_attributes (
        product_id INT,
        attribute VARCHAR(100) NOT NULL,
        attribute_quantity DECIMAL(10, 2),
        attribute_string VARCHAR(100),
        Foreign Key (product_id) References products(product_id)
        )
    """)

    return connection
