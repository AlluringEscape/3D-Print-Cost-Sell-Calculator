from tkinter import Toplevel, Label, Button, Listbox, Entry, END, messagebox
from utils import *

def open_consumable_settings(parent):
    consumables = load_data(CONSUMABLES_FILE)
    
    def refresh_listbox():
        listbox.delete(0, END)
        for cons in consumables:
            listbox.insert(END, f"{cons['name']} - ${cons['cost']}")

    def open_add_popup():
        add_window = Toplevel(parent)
        center_window(add_window, parent)
        add_window.title("Add Consumable")
        
        Label(add_window, text="Name:").grid(row=0, column=0)
        name_entry = Entry(add_window)
        name_entry.grid(row=0, column=1)
        
        Label(add_window, text="Cost per Use:").grid(row=1, column=0)
        cost_entry = Entry(add_window)
        cost_entry.grid(row=1, column=1)
        
        def save_consumable():
            try:
                consumables.append({
                    "name": name_entry.get().strip(),
                    "cost": float(cost_entry.get())
                })
                save_data(consumables, CONSUMABLES_FILE)
                refresh_listbox()
                add_window.destroy()
            except:
                messagebox.showerror("Error", "Invalid cost value")
        
        Button(add_window, text="Save", command=save_consumable).grid(row=2, columnspan=2)

    def remove_consumable():
        selected = listbox.curselection()
        if selected:
            consumables.pop(selected[0])
            save_data(consumables, CONSUMABLES_FILE)
            refresh_listbox()

    cons_window = Toplevel(parent)
    center_window(cons_window, parent)
    cons_window.title("Manage Consumables")
    
    listbox = Listbox(cons_window, width=40)
    listbox.pack(pady=10)
    refresh_listbox()
    
    Button(cons_window, text="Add", command=open_add_popup).pack(side="left", padx=10)
    Button(cons_window, text="Remove", command=remove_consumable).pack(side="right", padx=10)