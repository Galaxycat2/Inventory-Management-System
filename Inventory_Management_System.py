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


#Class for searching products
class Search_Products():
    # You should have only ONE __init__ method
    def __init__(self, inventory_instance):
        # Get the connection from the inventory instance
        self.inventory = inventory_instance
        self.connection = self.inventory.connection
        self.cursor = self.inventory.cursor
        
    #Method for Searching the Inventory by product name
    def search_products_by_name(self, product_name):
        db_query = "SELECT * FROM products WHERE product_name LIKE %s"
        search_param = f"%{product_name}%"
        self.cursor.execute(db_query, (search_param))
        products = self.cursor.fetchall()
    
        if products:
            print(f"Found {len(products)} products matching '{product_name}':")
            for product in products:
                print("\nProduct ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {}".format(
                    product[0], product[1], product[2], product[3], product[4]))
        else:
            print("No products matching search in the Inventory")
            
    #Method for Searching the Inventory by product ID
    def search_products_by_ID(self, product_id):
        db_query = "SELECT * FROM products WHERE product_id = %s"
        search_param = product_id
        self.cursor.execute(db_query, (search_param))
        products = self.cursor.fetchall()
    
        if products:
            print(f"Found {len(products)} products matching '{product_id}':")
            for product in products:
                print("\nProduct ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {}".format(
                    product[0], product[1], product[2], product[3], product[4]))
        else:
            print("No products matching search in the Inventory")
            
            
    #Method for Searching the Inventory by product category
    def search_products_by_category(self, category):
        db_query = "SELECT * FROM products WHERE category LIKE %s"
        search_param = f"%{category}%"
        self.cursor.execute(db_query, (search_param))
        products = self.cursor.fetchall()
    
        if products:
            print(f"Found {len(products)} products matching '{category}':")
            for product in products:
                print("\nProduct ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {}".format(
                    product[0], product[1], product[2], product[3], product[4]))
        else:
            print("No products matching search in the Inventory")
        
    
    
            
        
        
            

# Menu display
print("""
    1. Add Product
    2. Remove Product
    3. Update Product
    4. List Product
    5. Search Inventory
    6. Exit
""")



def get_string_type(prompt):
  
    
 
    while True:
        user_input = input(prompt)
        
        # Check if the input is numeric
        try:
            # Try to convert to float to catch both integers and decimals
            float(user_input)
            print("Invalid input! Please enter a string value, not a number.")
        except ValueError:
            # If conversion fails, it's not a number - which is what we want
            return user_input
       
            
            
def get_integer_type(prompt):
    
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid input! Please enter an integer value.")    

def get_float_type(prompt):
    
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid input! Please enter a float value.")  
            

inventory = Inventory()
choice = get_integer_type("Enter a choice. ")
updater = Update_products(inventory)
searcher = Search_Products(inventory)       
            
    

if choice == 1:
    result = None
    
    product_id = get_integer_type("Enter a product ID. ") 
    
        
    product_id_exist = "SELECT COUNT(*) FROM products WHERE product_id = %s"
    inventory.cursor.execute(product_id_exist,(product_id))
    result = inventory.cursor.fetchone()[0]
    if(result > 0):
        print("This product already exist in the inventory management system.")
        exit()
        
   
    product_name = get_string_type("Enter a product name: ")
        
    
    quantity = get_integer_type("Enter product quantity: ")
    
   
    price = get_float_type("Enter a product price. ")
    
    
    category = get_string_type("Enter product category: ")
  
    
    new_product = Product(product_id, product_name, quantity, price, category)
    
    print("Product {} is being added".format(product_id))
        
    inventory.add_product(new_product)
    print("Product {} is added".format(product_id))
 
elif choice == 2:
    product_id = get_integer_type("Enter product ID: ")
    
    print("{} is being removed\n".format(product_id))
    inventory.remove_product(product_id)
    print("Product {} is removed\n".format(product_id))
    
elif choice == 3:
      
    print("""
          1. Update price
          2. Update Quantity""")
    
    update_choice = int(input("Enter your choice: "))
    
    
    if(update_choice == 1):
        product_id = get_integer_type("Enter product ID: ")
        new_price = get_float_type("Enter the new price: ")
        updater.update_price(product_id, new_price)
        
    elif (update_choice == 2):
        product_id = get_integer_type("Enter product ID: ")
        new_quantity = get_integer_type("Enter the new quantity: ")
        updater.update_quantity(new_quantity, product_id)

    
    
elif choice == 4:
    print("Listing products....")
    
    inventory.list_products()
    
elif choice == 5:
    print("""
          1. Search by product name
          2. Search by product ID
          3. Search by product category""")
    search_choice = int(input("How would you like to search for an item?"))
    
    if(search_choice == 1):
        product_name = get_string_type("Enter product name: ")
        searcher.search_products_by_name(product_name)
    
            
     
    elif(search_choice == 2):
        product_id = get_integer_type("Enter product ID: ")
        searcher.search_products_by_ID(product_id)
        
    elif(search_choice == 3):
        category = get_string_type("Enter product category: ")
        searcher.search_products_by_category(category)
       
        
        
    

elif choice == 6:
    print("Exiting program...")

# Don't forget to close the connection when done
inventory.close_connection()