import schemas, product_inventory

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

    def DefaultSearch(self, query):
        try:
            self.search_products_by_name(query)
        except:
            try:
                self.search_products_by_category(query)
            except:
                try:
                    self.search_products_by_ID(query)
                except:
                    print("")