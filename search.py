import schemas, product_inventory
from tkinter import ttk, font
from tkinter import *
import tkinter as tk

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
        results = []

        if products:
            resultNum = 0
            print(f"Found {len(products)} products matching '{product_name}':")
            #result.set(value=f"Found {len(products)} products matching '{product_name}':")
            for product in products:
                results.append([])
                results[resultNum].append("\nProduct ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {}".format(
                    product[0], product[1], product[2], product[3], product[4]))
                resultNum+=1
                print("\nProduct ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {}".format(
                    product[0], product[1], product[2], product[3], product[4]))
                #result.set(value=(result.get() + "\nProduct ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {}".format(
                #    product[0], product[1], product[2], product[3], product[4])))
        else:
            print("No products matching search in the Inventory")
            results.append(["No products matching search in the Inventory"])
        return results
    
    #Method for Searching the Inventory by product ID
    def search_products_by_ID(self, product_id):
        db_query = "SELECT * FROM products WHERE product_id = %s"
        search_param = product_id
        self.cursor.execute(db_query, (search_param))
        products = self.cursor.fetchall()
        results = []
    
        if products:
            resultNum = 0
            print(f"Found {len(products)} products matching '{product_id}':")
            for product in products:
                results.append([])
                results[resultNum].append("\nProduct ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {}".format(
                    product[0], product[1], product[2], product[3], product[4]))
                resultNum+=1
                print("\nProduct ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {}".format(
                    product[0], product[1], product[2], product[3], product[4]))
        else:
            print("No products matching search in the Inventory")
            results.append(["No products matching search in the Inventory"])
        return results
            
            
    #Method for Searching the Inventory by product category
    def search_products_by_category(self, category):
        db_query = "SELECT * FROM products WHERE category LIKE %s"
        search_param = f"%{category}%"
        self.cursor.execute(db_query, (search_param))
        products = self.cursor.fetchall()
        results = []

        if products:
            resultNum = 0
            print(f"Found {len(products)} products matching '{category}':")
            for product in products:
                results.append([])
                results[resultNum].append("\nProduct ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {}".format(
                    product[0], product[1], product[2], product[3], product[4]))
                resultNum+=1
                print("\nProduct ID: {}\nProduct Name: {}\nProduct Quantity: {}\nProduct Price: {}\nProduct Category: {}".format(
                    product[0], product[1], product[2], product[3], product[4]))
                
        else:
            print("No products matching search in the Inventory")
            results.append(["No products matching search in the Inventory"])
        return results
