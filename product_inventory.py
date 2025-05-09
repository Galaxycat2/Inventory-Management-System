import pymysql
from schemas import DatabaseSetup



# Create a product constructor
class Product():
    def __init__(self, product_id, product_name, quantity, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.category = category
    
    # Returns a formated string when printing object
    def __str__(self):
            return "Product ID: {}\nProduct Name: {}\nQuantity: {}\nPrice: {}\nCategory: {}\n".format(
                self.product_id, self.product_name, self.quantity, self.price, self.category)
        
# Class to handle inventory operations like adding/removing/listing   
class Inventory():
    def __init__(self):
        # Initialize database connection in the constructor
        self.connection = DatabaseSetup()
        self.cursor = self.connection.cursor()
                
    # Method to add a product
    def add_product(self, product):
        
    
        query = "INSERT INTO products(product_id, product_name, quantity, price, category) VALUES (%s,%s,%s,%s,%s)"
        self.cursor.execute(query,(product.product_id, product.product_name, product.quantity, product.price, product.category))
        self.connection.commit()
        print(f"Product '{product.product_name}' added successfully!")
        return (f"Product '{product.product_name}' added successfully!")
        
           
            
    # Method to delete products
    def remove_product(self, product_id):
        query = "DELETE FROM products WHERE product_id = %s"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()
        print(f"Product with ID '{product_id}' deleted successfully!")
        return (f"Product with ID '{product_id}' deleted successfully!")
        
    # Method to List all products
    def list_products(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        result = []
        if rows: 
            for row in rows:
                result.append(f"Product ID: {row[0]}\nProduct Name: {row[1]}\nProduct Quantity: {row[2]}\nProduct Price: {row[3]}\nProduct Category: {row[4]} ")
                print("Product ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {} ".format(row[0],row[1],row[2],row[3],row[4]))
        else:
            result.append("No products in the Inventory")
            print("No products in the Inventory")
        return result
                     
# Method to close the connection
    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

inventory =Inventory()

