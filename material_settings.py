from tkinter import Toplevel, Label, Button, Listbox, Entry, END, messagebox
from utils import load_data, save_data, MATERIALS_FILE

def open_material_settings(parent):
    materials = load_data(MATERIALS_FILE)
    
    def refresh_listbox():
        listbox.delete(0, END)
        for material in materials:
            listbox.insert(END, f"{material['name']} - ${material['cost_per_gram']}/g")
    
    def open_add_material_popup():
        add_window = Toplevel(parent)
        add_window.title("Add Material")
        
        Label(add_window, text="Material Name:").grid(row=0, column=0)
        name_entry = Entry(add_window)
        name_entry.grid(row=0, column=1)
        
        Label(add_window, text="Cost per Gram ($):").grid(row=1, column=0)
        cost_entry = Entry(add_window)
        cost_entry.grid(row=1, column=1)
        
        def add_material():
            materials.append({
                "name": name_entry.get(),
                "cost_per_gram": float(cost_entry.get())
            })
            save_data(materials, MATERIALS_FILE)
            refresh_listbox()
            add_window.destroy()
        
        Button(add_window, text="Add", command=add_material).grid(row=2, columnspan=2)
    
    def remove_material():
        selected = listbox.curselection()
        if selected:
            materials.pop(selected[0])
            save_data(materials, MATERIALS_FILE)
            refresh_listbox()
    
    material_window = Toplevel(parent)
    material_window.title("Material Settings")
    
    listbox = Listbox(material_window, width=40)
    listbox.pack()
    refresh_listbox()
    
    Button(material_window, text="Add Material", command=open_add_material_popup).pack()
    Button(material_window, text="Remove Selected", command=remove_material).pack()