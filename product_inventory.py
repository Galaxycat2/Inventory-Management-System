import pymysql
from schemas import sqlpass, inventory_name
from update import Update_products
from search import Search_Products


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
            password=sqlpass,
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

inventory =Inventory()
updater = Update_products(inventory)
searcher = Search_Products(inventory) 