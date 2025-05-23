#Standard Library Imports
import pymysql
from tk import *

#Class Files
from product_inventory import Inventory, Product
from schemas import *
from update import Update_products, updater
from search import Search_Products, searcher
from input_valid import *


DatabaseSetup()
MainWindow() 

inventory = Inventory()     # Creates an Inventory object

# Menu display in Control Window
print("""
    1. Add Product
    2. Remove Product
    3. Update Product
    4. List Product
    5. Search Inventory
    6. Exit
""")

choice = get_integer_type("Enter a choice: ")   # Gets the users input
      
    
#Command Window Prompts and User actions
while (choice != 6):

     # Option 1: Add a new product
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
    
    # Option 2: Remove an existing product
    elif choice == 2:
        product_id = get_integer_type("Enter product ID: ")
        
        print("{} is being removed\n".format(product_id))
        inventory.remove_product(product_id)
        print("Product {} is removed\n".format(product_id))
        
     # Option 3: Update Product
    elif choice == 3:
        
        #Display Update Menu
        print("""
            1. Update price
            2. Update Quantity
            3. Add attribute""")
        
        update_choice = int(input("Enter your choice: "))
        
        
        if(update_choice == 1):
            product_id = get_integer_type("Enter product ID: ")
            new_price = get_float_type("Enter the new price: ")
            updater.update_price(product_id, new_price)
            
        elif (update_choice == 2):
            product_id = get_integer_type("Enter product ID: ")
            new_quantity = get_integer_type("Enter the new quantity: ")
            updater.update_quantity(new_quantity, product_id)
        
        elif (update_choice == 3):
            product_id = int(input("Enter product ID: "))
            attribute = str(input("Enter Attribute name: "))
            attribute_value = str(input("Enter Attribute value (integer or string): "))
            try:
                attribute_qnt = int(attribute_value)
                updater.addAttribute(product_id, attribute, attribute_qnt)
            except:
                updater.addAttribute(product_id, attribute, attribute_value)
  
    #Option 4: List Products
    elif choice == 4:
        print("Listing products....")
        
        inventory.list_products()
        
    #Option 5: Search Inventory
    elif choice == 5:

        #Display Search Menu
        print("""
            1. Search by product name
            2. Search by product ID
            3. Search by product category""")
        
        #Get User Input
        search_choice = int(input("How would you like to search for an item?"))
        
        #Search by name
        if(search_choice == 1):
            product_name = get_string_type("Enter product name: ")
            searcher.search_products_by_name(product_name)
        
        #Search by ID
        elif(search_choice == 2):
            product_id = get_integer_type("Enter product ID: ")
            searcher.search_products_by_ID(product_id)
            
        #Search by category
        elif(search_choice == 3):
            category = get_string_type("Enter product category: ")
            searcher.search_products_by_category(category)
    
    # Option 6: Exit the program
    elif choice == 6:
        print("Exiting program...")

    choice = get_integer_type("Enter a choice: ")

# Don't forget to close the connection when done
inventory.close_connection()