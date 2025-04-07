import pymysql
import pymysql.cursors

# Connect to the MySQL database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Iondragonfly23!",
    database="inventory_db",
    cursorclass=pymysql.cursors.DictCursor 
)


cursor = connection.cursor()
    
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

# Close the connection
connection.close()

# print("Table 'products' created successfully!")

# Create a product constructor
class Product():
    def __init__(self, product_id, product_name, quantity, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.category = category
    
    def __str__(self):
            return "Product ID: {}\nProduct Name: {}\nQuantity: {}\nPrice: {}\nCategory: {}\n".format(
                self.product_id, self.product_name, self.quantity, self.price, self.category)
        

class Inventory():
    def __init__(self):
        # Initialize database connection in the constructor
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="Iondragonfly23!",
            database="inventory_db",
            cursorclass=pymysql.cursors.DictCursor #sets cursor to return dictionary objects
        )
        self.cursor = self.connection.cursor()
                
    # Method to add a product
    def add_product(self, product: Product):
        query = "INSERT INTO products(product_id, product_name, quantity, price, category) VALUES (%s,%s,%s,%s,%s)"
        self.cursor.execute(query,(product.product_id, product.product_name, product.quantity, product.price, product.category))
        self.connection.commit()
        print(f"Product '{product.product_name}' added successfully!")
            
    # Method to delete products
    def remove_product(self, product_id):
        query = "DELETE FROM products WHERE product_id = %s"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()
        print(f"Product with ID '{product_id}' deleted successfully!")
        
    # Method to List all products
    def list_products(self):
        query = "SELECT `product_id`, `product_name`, `quantity`, `price`,`category` FROM products"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if rows: 
            for row in rows:
                print(f'Product ID: {row["product_id"]}\nProduct Name: {row["product_name"]}\nProduct Quantity: {row["quantity"]}\nProduct Price: {row["price"]}\nProduct Category: {row["category"]} ')
        else:
            print("No products in the Inventory")
    
    #Method for Searching the Inventory
    def search_products(self, query):
        db_query = "SELECT * FROM products"
        self.cursor.execute(db_query)
        products = self.cursor.fetchall()
        results = []
        for product in products:
            if ((query.lower() in product["product_name"].lower()) or(query.lower() in product["category"].lower())):
                results.append(product)
        if results:
            for product in results:
                print(f'Product ID: {product["product_id"]}\nProduct Name: {product["product_name"]}\nProduct Quantity: {product["quantity"]}\nProduct Price: {product["price"]}\nProduct Category: {product["category"]} ')
        else:
            print("No products matching search in the Inventory")

    
    # Method to close the connection
    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

# Menu display
print("""
    1. Add product
    2. Remove product
    3. List products
    4. Search inventory
    5. Exit
""")

inventory = Inventory()
choice = int(input("Enter your choice: "))
    
if choice == 1:
    product_id = int(input("Enter product ID: "))
    product_name = str(input("Enter product name: "))
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    category = str(input("Enter product category: "))
    new_product = Product(product_id, product_name, quantity, price, category)
    
    print("Product {} is being added".format(product_id))
        
    inventory.add_product(new_product)
    print("Product {} is added".format(product_id))
 
elif choice == 2:
    product_id = input("Enter product ID: ")
    
    print("{} is being removed\n".format(product_id))
    inventory.remove_product(product_id)
    print("Product {} is removed\n".format(product_id))
    
elif choice == 3:
    print("Listing products....")
    
    inventory.list_products()

elif choice == 4:
    search = input("Enter search: ")
    inventory.search_products(search)


elif choice == 5:
    print("Exiting program...")
'''elif choice == 4:
    print("Exiting program...")
'''
# Don't forget to close the connection when done
inventory.close_connection()