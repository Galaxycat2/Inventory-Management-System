import pymysql   

# Connect to the MySQL database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Arriaiscute100#",
    database="inventory_db"
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
            password="Arriaiscute100#",
            database="inventory_db"
        )
        self.cursor = self.connection.cursor()
                
    # Method to add a product
    def add_product(self, product):
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
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if rows: 
            for row in rows:
                print("Product ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {} ".format(row[0],row[1],row[2],row[3],row[4]))
        else:
            print("No products in the Inventory")
# Method to close the connection
    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")
    
    #Class for updating products
class Update_products():
    # You should have only ONE __init__ method
    def __init__(self, inventory_instance):
        # Get the connection from the inventory instance
        self.inventory = inventory_instance
        self.connection = self.inventory.connection
        self.cursor = self.inventory.cursor
        
            
    def update_price(self, product_id, new_price):
        query = "UPDATE products SET price = %s WHERE product_id = %s"
        self.cursor.execute(query, (product_id,new_price))
        self.connection.commit()
        print(f"Product with ID '{product_id}' price updated to '${new_price}' successfully!")
            
    def update_quantity(self, product_id, new_quantity):
        query = "UPDATE products SET quantity = %s WHERE product_id = %s"
        self.cursor.execute(query, (product_id, new_quantity))
        self.connection.commit()
        print(f"Product with ID '{product_id}' quantity updated to '{new_quantity}' successfully!")
            
        
        
            

# Menu display
print("""
    1. Add product
    2. Remove product
    3. Update product
    4. List product
    5. Exit
""")

inventory = Inventory()
choice = int(input("Enter your choice: "))
updater = Update_products(inventory)
    
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
      
    print("""
          1. Update price
          2. Update Quantity""")
    
    update_choice = int(input("Enter your choice: "))
    
    
    if(update_choice == 1):
        product_id = int(input("Enter product ID: "))
        new_price = float(input("Enter the new price: "))
        updater.update_price(product_id, new_price)
        
    elif (update_choice == 2):
        product_id = int(input("Enter product ID: "))
        new_quantity = int(input("Enter the new quantity: "))
        updater.update_quantity(new_quantity, product_id)

    
    
elif choice == 4:
    print("Listing products....")
    
    inventory.list_products()

elif choice == 5:
    print("Exiting program...")

# Don't forget to close the connection when done
inventory.close_connection()