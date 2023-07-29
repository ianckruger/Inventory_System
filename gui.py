import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from inventorySystem import *

inv = InventorySystem()

def handle_add():
    item_name = item_entry.get()
    item_quant = quantity_entry.get()

    if item_name and item_quant:
        try:
            item_quant = int(item_quant)
            if item_quant > 0:
                inv.addItem(item_name,item_quant)
                messagebox.showinfo("Item Added", f"{item_quant} {item_name} added to the inventory")
                item_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Invalid Quantity", "Quantity must be positive.")
        except ValueError:
            messagebox.showerror({"Invalid, not positive number."})
    else:
        messagebox.showerror("Missing information.")



def handle_search():
    question = search_entry.get()
    if question:
        results_treeview.delete(*results_treeview.get_children())

        results = search_item(question)
        if results:
            for item, quantity in results:
                results_treeview.insert("","end", values=(item, quantity))
        else:
            messagebox.showinfo("No results", "No matching items found.")
    else:
        messagebox.showinfo("Empty search", "Please enter a search query.")

def search_item(query):
    return inv.searchByName(query)        

window = tk.Tk()
window.title("Inventory System")

item_label = tk.Label(window, text="Item:")
item_label.pack()

item_entry = tk.Entry(window)
item_entry.pack()

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()

quantity_entry = tk.Entry(window)
quantity_entry.pack()

search_label = tk.Label(window, text="Search for item:")
search_label.pack()
search_entry = tk.Entry(window)
search_entry.pack()

results_treeview = ttk.Treeview(window, columns=("Item", "Quantity"))
results_treeview.heading("#1", text="Item")
results_treeview.heading('#2', text="Quantity")
results_treeview.pack()

search_button = tk.Button(window, text="Search", command=handle_search)
search_button.pack()

add_button = tk.Button(window,text="Add Item", command=handle_add)
add_button.pack()

window.mainloop()
