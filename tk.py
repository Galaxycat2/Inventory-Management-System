from tkinter import *
from tkinter import ttk, font
from product_inventory import Product, Inventory, inventory, updater, searcher
from search import Search_Products
from schemas import inventory_name
import tkinter as tk

root = Tk()
root.title("InventorEase")
root.geometry("800x600")
root.columnconfigure(0, weight=2)
root.rowconfigure(0,weight=2)

resultList = []

#Styling
titleFont = font.Font(size=16,weight="bold")
subTitleFont = font.Font(size=13,weight="bold",slant="italic")

def MainWindow():
    mainframe = ttk.Frame(root, padding="3 3 12 12", width=1000, height=1000)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure([1,2,3,4,5,6],weight=1)
    mainframe.rowconfigure([2,3,4,5], weight=1)
    main_title = ttk.Label(mainframe, text=f'Inventorease', font=titleFont)
    main_title.grid(column=3, row=1, columnspan=2)

    inventory_title = ttk.Label(mainframe, text=inventory_name, font=subTitleFont)
    inventory_title.grid(column=3, row=2, columnspan=2)
    
    view_inventory_button = ttk.Button(mainframe, width=7, text="View Inventory", command=inventory.list_products)
    view_inventory_button.grid(column=2, row=3, sticky=(W, E))

    search_inventory_button = ttk.Button(mainframe, width=7, text="Search", command=SearchWindow)
    search_inventory_button.grid(column=3, row=3, sticky=(W, E))

    add_item_button = ttk.Button(mainframe, width=7, text="Add Item")
    add_item_button.grid(column=4, row=3, sticky=(W, E))

    remove_item_button = ttk.Button(mainframe, width=7, text="Update item")
    remove_item_button.grid(column=5, row=3, sticky=(W, E))

def SearchWindow():

    root.children.clear()
    searchFrame = ttk.Frame(root, padding="3 3 12 12")
    searchFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    searchFrame.columnconfigure([1,2,3,4,5],weight=1)
    searchFrame.rowconfigure([1,2,3,4,5], weight=1)

    search_title = ttk.Label(searchFrame, text=f'Search Inventory: {inventory_name}')
    search_title.grid(column=2, row=1, columnspan=3)

    searchField_query = StringVar()
    searchField = ttk.Entry(searchFrame, textvariable=searchField_query).grid(column=2,row=2, columnspan=3, sticky="we")
    resultField = tk.Canvas(searchFrame)
    resultField.grid(column=2, columnspan=3, row=4, rowspan=2, sticky=(N, E, W, S))
    search_by_id_button = ttk.Button(searchFrame, width=7, text="Search By ID", command=lambda: searchIDandListResults(resultField, searchField_query.get()))
    search_by_id_button.grid(column=2, row=3, sticky=(W, E))
    search_by_name_button = ttk.Button(searchFrame, width=7, text="Search By Name", command=lambda: searchNameandListResults(resultField, searchField_query.get()))
    search_by_name_button.grid(column=3, row=3, sticky=(W, E))
    search_by_category_button = ttk.Button(searchFrame, width=7, text="Search By Product Category", command=lambda: searchCategoryandListResults(resultField, searchField_query.get()))
    search_by_category_button.grid(column=4, row=3, sticky=(W, E))

def searchNameandListResults(window,query):
    results = searcher.search_products_by_name(query)
    ListResults(window, results)

def searchIDandListResults(window,query):
    results = searcher.search_products_by_ID(query)
    ListResults(window, results)

def searchCategoryandListResults(window,query):
    results = searcher.search_products_by_category(query)
    ListResults(window, results)

def ListResults(window, results):
    window.children.clear()
    result_entries = 1
    for result in results:
        AddLabel(window, result[0], result_entries)
        result_entries+=1

def AddLabel(window, result, rowNum):
    label_text = result
    label = tk.Label(window, text=label_text)
    label.grid(column=1,row=rowNum, sticky=(N,W,E,S))

