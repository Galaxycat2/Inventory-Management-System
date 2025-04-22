from product_inventory import *
from schemas import cursor

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

    def update_product(self, product):
        query = "UPDATE products SET product_name = %s, price = %s, quantity = %s, category = %s WHERE product_id = %s"
        self.cursor.execute(query, (product.product_name, product.price, product.quantity, product.category, product.product_id))
        self.connection.commit()
        return(f"Product with ID: '{product.product_id}' updated successfully!")

    def addAttribute(self, product_id, attribute, attribute_value):
        if (attribute_value is not int):
            query = f'INSERT INTO product_attributes (product_id, attribute, attribute_string) VALUES ("{product_id}","{attribute}","{attribute_value}");'
            self.cursor.execute(query)
            self.connection.commit()
        else:
            query = f'INSERT INTO product_attributes (product_id, attribute, attribute_quantity) VALUES ("{product_id}","{attribute}","{attribute_value}");'
            self.cursor.execute(query)
            self.connection.commit()

updater = Update_products(inventory)
