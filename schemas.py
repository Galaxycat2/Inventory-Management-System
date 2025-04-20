import pymysql

sqlpass = "Iondragonfly23!"
inventory_name = "inventory_db"
# Connect to the MySQL database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=sqlpass,
    database=inventory_name
)

cursor = connection.cursor()

def DatabaseSetup():
        
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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_attributes (
        product_id INT,
        attribute VARCHAR(100) NOT NULL,
        attribute_quantity DECIMAL(10, 2),
        attribute_string VARCHAR(100),
        Foreign Key (product_id) References products(product_id)
        )
    """)

    # Close the connection
    connection.close()

# print("Table 'products' created successfully!")