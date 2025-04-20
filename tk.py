from tkinter import *
from tkinter import ttk
from product_inventory import *
from search import Search_Products

root = Tk()
root.title("InventorEase")
inventory = Inventory()
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=2)
root.rowconfigure(0,weight=2)

def MainWindow():
    mainframe = ttk.Frame(root, padding="3 3 12 12", width=1000, height=1000)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure([2,3,4,5],weight=1)
    mainframe.rowconfigure([2,3,4,5], weight=1)
    main_title = ttk.Label(mainframe, text=f'Inventorease')
    main_title.grid(column=3, row=1, columnspan=2)

    inventory_title = ttk.Label(mainframe, text=inventory_name)
    inventory_title.grid(column=3, row=2, columnspan=2)
    
    view_inventory_button = ttk.Button(mainframe, width=7, text="View Inventory", command=inventory.list_products)
    view_inventory_button.grid(column=2, row=3, sticky=(W, E))

    search_inventory_button = ttk.Button(mainframe, width=7, text="Search", command=SearchWindow)
    search_inventory_button.grid(column=3, row=3, sticky=(W, E))

    add_item_button = ttk.Button(mainframe, width=7)
    add_item_button.grid(column=4, row=3, sticky=(W, E))

    remove_item_button = ttk.Button(mainframe, width=7)
    remove_item_button.grid(column=5, row=3, sticky=(W, E))

def SearchWindow():

    mainframe.destroy()
    searchFrame = ttk.Frame(root, padding="3 3 12 12")
    searchFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=2)
    root.rowconfigure(0, weight=2)
    search_title = ttk.Label(searchFrame, text=f'Search Inventory')
    search_title.grid(column=3, row=1, columnspan=2)
    searchField_query = StringVar
    searchField = ttk.Entry(searchFrame, textvariable=searchField_query).grid(column=1,row=1, sticky="w")
