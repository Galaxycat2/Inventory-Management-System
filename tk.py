from tkinter import *
from tkinter import ttk, font
from product_inventory import Product, Inventory, inventory
from search import Search_Products, searcher
from update import Update_products, updater
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
    root.children.clear()
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure([1,2,3,4,5,6],weight=1)
    mainframe.rowconfigure([2,3,4,5], weight=1)
    main_title = ttk.Label(mainframe, text=f'Inventorease', font=titleFont)
    main_title.grid(column=3, row=1, columnspan=2)

    inventory_title = ttk.Label(mainframe, text=inventory_name, font=subTitleFont)
    inventory_title.grid(column=3, row=2, columnspan=2)
    
    view_inventory_button = ttk.Button(mainframe, width=7, text="View Inventory", command=ListProductsWindow)
    view_inventory_button.grid(column=2, row=3, sticky=(W, E))

    search_inventory_button = ttk.Button(mainframe, width=7, text="Search", command=SearchWindow)
    search_inventory_button.grid(column=3, row=3, sticky=(W, E))

    add_item_button = ttk.Button(mainframe, width=7, text="Add Item", command=AddItemWindow)
    add_item_button.grid(column=4, row=3, sticky=(W, E))

    remove_item_button = ttk.Button(mainframe, width=7, text="Update item", command=FindItemToUpdate)
    remove_item_button.grid(column=5, row=3, sticky=(W, E))

def SearchWindow():
    root.children.clear()
    searchFrame = ttk.Frame(root, padding="3 3 12 12")
    searchFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    searchFrame.columnconfigure([1,2,3,4,5],weight=1)
    searchFrame.rowconfigure([1,2,3,4,5], weight=1)

    backButton = ttk.Button(searchFrame, text="Back", command=MainWindow)
    backButton.grid(row=1,column=0)

    search_title = ttk.Label(searchFrame, text=f'Search Inventory: {inventory_name}')
    search_title.grid(column=2, row=1, columnspan=3)

    searchField_query = StringVar()
    searchField = ttk.Entry(searchFrame, textvariable=searchField_query).grid(column=2,row=2, columnspan=3, sticky="we")
    resultField = tk.Canvas(searchFrame)
    resultField.children.clear()
    resultField.grid(column=2, columnspan=3, row=4, rowspan=2, sticky=(N, E, W, S))
    resultField.columnconfigure([0], weight=1)
    search_by_id_button = ttk.Button(searchFrame, width=7, text="Search By ID", command=lambda: searchIDandListResults(resultField, searchField_query.get()))
    search_by_id_button.grid(column=2, row=3, sticky=(W, E))
    search_by_name_button = ttk.Button(searchFrame, width=7, text="Search By Name", command=lambda: searchNameandListResults(resultField, searchField_query.get()))
    search_by_name_button.grid(column=3, row=3, sticky=(W, E))
    search_by_category_button = ttk.Button(searchFrame, width=7, text="Search By Product Category", command=lambda: searchCategoryandListResults(resultField, searchField_query.get()))
    search_by_category_button.grid(column=4, row=3, sticky=(W, E))

def ListProductsWindow():
    root.children.clear()
    listProductsFrame = ttk.Frame(root, padding="3 3 12 12")
    listProductsFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    listProductsFrame.columnconfigure([1,2,3,4,5], weight=1)
    listProductsFrame.rowconfigure([1,2,3,4], weight=1)
    backButton = ttk.Button(listProductsFrame, text="Back", command=MainWindow)
    backButton.grid(row=1,column=1)

    listView_title = ttk.Label(listProductsFrame, text=f'View All: {inventory_name}', font=titleFont)
    listView_title.grid(column=2, row=1, columnspan=3)

    productsField = tk.Canvas(listProductsFrame)
    productsField.grid(row=2,column=2,columnspan=3,rowspan=3)

    result = inventory.list_products()
    rowcnt = 0
    colcnt = 0
    for rslt in result:
        GridLabel(productsField, rslt, rowcnt, colcnt)
        if colcnt == 2:
            colcnt = 0
            rowcnt +=1
        else:
            colcnt += 1

def AddItemWindow():
    root.children.clear()
    AddItemFrame = ttk.Frame(root, padding="3 3 12 12")
    AddItemFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    AddItemFrame.columnconfigure([1,4], weight=1)
    AddItemFrame.columnconfigure([2,3], weight=3)
    AddItemFrame.rowconfigure([1,2,3,4], weight=1)
    backButton = ttk.Button(AddItemFrame, text="Back", command=MainWindow)
    backButton.grid(row=1,column=1)
    Add_Item_title = ttk.Label(AddItemFrame, text="Add Products", font=titleFont)
    Add_Item_title.grid(row=1, column=2, columnspan=2)
    add_item_form = tk.Frame(AddItemFrame)
    add_item_form.grid(column=2, row=2, rowspan=3, sticky="new")
    item_name_label = ttk.Label(add_item_form, text="Product Name:")
    item_name_label.grid(row=1, column=1, pady=5)
    item_name = StringVar()
    item_name_entry = ttk.Entry(add_item_form, textvariable=item_name)
    item_name_entry.grid(row=1, column=2, pady=5)
    item_ID_label = ttk.Label(add_item_form, text="Product ID:")
    item_ID_label.grid(row=2, column=1, pady=5)
    item_ID = StringVar()
    item_ID_entry = ttk.Entry(add_item_form, textvariable=item_ID)
    item_ID_entry.grid(row=2, column=2, pady=5)
    item_Quant_label = ttk.Label(add_item_form, text="Product Quantity:")
    item_Quant_label.grid(row=3, column=1, pady=5)
    item_quant = StringVar()
    item_quant_entry = ttk.Entry(add_item_form, textvariable=item_quant)
    item_quant_entry.grid(row=3, column=2, pady=5)
    item_price_label = ttk.Label(add_item_form, text="Product Price ($):")
    item_price_label.grid(row=4, column=1, pady=5)
    item_price = StringVar()
    item_price_entry = ttk.Entry(add_item_form, textvariable=item_price)
    item_price_entry.grid(row=4, column=2, pady=5)
    item_category_label = ttk.Label(add_item_form, text="Product Category:")
    item_category_label.grid(row=5, column=1, pady=5)
    item_category = StringVar()
    item_category_entry = ttk.Entry(add_item_form, textvariable=item_category)
    item_category_entry.grid(row=5, column=2, pady=5)
    resultField = ttk.Frame(AddItemFrame)
    resultField.grid(column=3, row=2, rowspan=2)
    add_button = ttk.Button(add_item_form, text="Add Product", command= lambda: Add_item(item_ID.get(), item_name.get(), item_quant.get(), item_price.get(), item_category.get(), resultField))
    add_button.grid(row=6, pady=30)

def FindItemToUpdate():
    root.children.clear()
    UpdateItemFrame = ttk.Frame(root, padding="3 3 12 12")
    UpdateItemFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    UpdateItemFrame.columnconfigure([1,4], weight=1)
    UpdateItemFrame.columnconfigure([2,3], weight=3)
    UpdateItemFrame.rowconfigure([1,2,3,4], weight=1)
    backButton = ttk.Button(UpdateItemFrame, text="Back", command=MainWindow)
    backButton.grid(row=1,column=1)
    Update_Item_title = ttk.Label(UpdateItemFrame, text="Update Products", font=titleFont)
    Update_Item_title.grid(row=1, column=2, columnspan=2)
    productIDLabel = ttk.Label(UpdateItemFrame, text="Enter ID for Product to Update:")
    productIDLabel.grid(row=2, column=2, sticky="ew")
    productID = StringVar()
    productIDEntry = ttk.Entry(UpdateItemFrame, textvariable=productID)
    productIDEntry.grid(row=2, column=3)
    ErrorFrame = ttk.Frame(UpdateItemFrame)
    ErrorFrame.grid(row=4, column=2, columnspan=2)
    updateButton = ttk.Button(UpdateItemFrame, text="Update Product", command= lambda: UpdateProductWindow(productID.get(), ErrorFrame))
    updateButton.grid(row=3, column=2, pady=10)
    deleteButton = ttk.Button(UpdateItemFrame, text="Delete Item", command= lambda: DeleteProduct(productID.get(), ErrorFrame))
    deleteButton.grid(row=3, column=3, pady=10)



def UpdateProductWindow(productID, ErrorFrame):
    product = searcher.get_product_by_ID(productID)
    if type(product) == str:
        errorLabel = ttk.Label(ErrorFrame, text=product)
        errorLabel.grid(sticky="ew")
        return
    else:
        root.children.clear()
        UpdateItemFrame = ttk.Frame(root, padding="3 3 12 12")
        UpdateItemFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        UpdateItemFrame.columnconfigure([1,4], weight=1)
        UpdateItemFrame.columnconfigure([2,3], weight=3)
        UpdateItemFrame.rowconfigure([1,2,3,4], weight=1)
        backButton = ttk.Button(UpdateItemFrame, text="Back", command=FindItemToUpdate)
        backButton.grid(row=1,column=1)
        Add_Item_title = ttk.Label(UpdateItemFrame, text=f"Update Product ID: {product.product_id}", font=titleFont)
        Add_Item_title.grid(row=1, column=2, columnspan=2)
        add_item_form = tk.Frame(UpdateItemFrame)
        add_item_form.grid(column=2, row=2, rowspan=3, sticky="new")
        item_ID_label = ttk.Label(add_item_form, text=f"Product ID: {product.product_id}")
        item_ID_label.grid(row=1, column=1, pady=5)
        item_name_label = ttk.Label(add_item_form, text="Product Name:")
        item_name_label.grid(row=2, column=1, pady=5)
        item_name = StringVar(value=product.product_name)
        item_name_entry = ttk.Entry(add_item_form, textvariable=item_name)
        item_name_entry.grid(row=2, column=2, pady=5)
        item_Quant_label = ttk.Label(add_item_form, text="Product Quantity:")
        item_Quant_label.grid(row=3, column=1, pady=5)
        item_quant = StringVar(value=product.quantity)
        item_quant_entry = ttk.Entry(add_item_form, textvariable=item_quant)
        item_quant_entry.grid(row=3, column=2, pady=5)
        item_price_label = ttk.Label(add_item_form, text="Product Price ($):")
        item_price_label.grid(row=4, column=1, pady=5)
        item_price = StringVar(value=product.price)
        item_price_entry = ttk.Entry(add_item_form, textvariable=item_price)
        item_price_entry.grid(row=4, column=2, pady=5)
        item_category_label = ttk.Label(add_item_form, text="Product Category:")
        item_category_label.grid(row=5, column=1, pady=5)
        item_category = StringVar(value=product.category)
        item_category_entry = ttk.Entry(add_item_form, textvariable=item_category)
        item_category_entry.grid(row=5, column=2, pady=5)
        resultField = ttk.Frame(UpdateItemFrame)
        resultField.grid(column=3, row=2, rowspan=2)
        update_button = ttk.Button(add_item_form, text="Update Product", command= lambda: Update_item(product.product_id, item_name.get(), item_quant.get(), item_price.get(), item_category.get(), resultField))
        update_button.grid(row=6, column=1, pady=30)
        deleteButton = ttk.Button(add_item_form, text="Delete Item", command= lambda: DeleteProduct(product.product_id, resultField))
        deleteButton.grid(row=6, column=2, pady=30)


def Add_item(id, name, quant, price, category, frame):
    frame.children.clear()
    new_product = Product(id, name, quant, price, category)
    result = inventory.add_product(new_product)
    resultLabel = ttk.Label(frame, text=result, wraplength=200, font=subTitleFont)
    resultLabel.grid(column=0, row=0)

def DeleteProduct(id, frame):
    frame.children.clear()
    result = inventory.remove_product(id)
    resultLabel = ttk.Label(frame, text=result, wraplength=200, font=subTitleFont)
    resultLabel.grid(column=0, row=0)

def Update_item(id, name, quant, price, category, frame):
    try: 
        int(id)
        float(price)
        int(quant)
        frame.children.clear()
        new_product = Product(id, name, quant, price, category)
        result = updater.update_product(new_product)
        resultLabel = ttk.Label(frame, text=result, wraplength=200, font=subTitleFont)
        resultLabel.grid(column=0, row=0)
    except:
        ErrorLabel = ttk.Label(frame, text="Error: Invalid inputs, Price and Quantity should be a whole number, Price should be a value with two decimal places.", wraplength=200, font=subTitleFont)
        ErrorLabel.grid(column=0, row=0)


def searchNameandListResults(window,query):
    window.children.clear()
    results = searcher.search_products_by_name(query)
    ListResults(window, results)

def searchIDandListResults(window,query):
    try:
        int(query)
        window.children.clear()
        results = searcher.search_products_by_ID(query)
        ListResults(window, results)
    except:
        resultLabel = ttk.Label(window, text=f"Error: Invalid ID", wraplength=200, font=subTitleFont)
        resultLabel.grid(column=0, row=0)


def searchCategoryandListResults(window,query):
    window.children.clear()
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
    label.grid(column=0,row=rowNum, columnspan=3, sticky=(N,W,E,S))

def GridLabel(window, result, rowNum, colNum):
    label_text = result
    label = tk.Label(window, text=label_text)
    label.grid(column=colNum,row=rowNum, sticky=(N,W,E,S))
