from tkinter import Toplevel, Label, Button, Listbox, Entry, END, messagebox, ttk
from utils import *

def open_material_settings(parent):
    materials = load_data(MATERIALS_FILE)
    
    def refresh_listbox():
        listbox.delete(0, END)
        for mat in materials:
            listbox.insert(END, f"{mat['brand']} ({mat['type']}) - ${mat['cost_per_gram']}/g")

    def open_add_popup():
        add_window = Toplevel(parent)
        center_window(add_window, parent)
        add_window.title("Add Material")
        
        Label(add_window, text="Brand:").grid(row=0, column=0, padx=5, pady=5)
        brand_entry = Entry(add_window)
        brand_entry.grid(row=0, column=1, padx=5, pady=5)
        
        Label(add_window, text="Type:").grid(row=1, column=0, padx=5, pady=5)
        type_combo = ttk.Combobox(add_window, values=["FDM", "Resin"], state="readonly")
        type_combo.grid(row=1, column=1, padx=5, pady=5)
        
        Label(add_window, text="Cost/Gram ($):").grid(row=2, column=0, padx=5, pady=5)
        cost_entry = Entry(add_window)
        cost_entry.grid(row=2, column=1, padx=5, pady=5)

        def save_material():
            try:
                materials.append({
                    "brand": brand_entry.get().strip(),
                    "type": type_combo.get(),
                    "cost_per_gram": float(cost_entry.get())
                })
                save_data(materials, MATERIALS_FILE)
                refresh_listbox()
                add_window.destroy()
            except:
                messagebox.showerror("Error", "Invalid values")

        Button(add_window, text="Save", command=save_material).grid(row=3, columnspan=2)

    def remove_material():
        selected = listbox.curselection()
        if selected:
            materials.pop(selected[0])
            save_data(materials, MATERIALS_FILE)
            refresh_listbox()

    mat_window = Toplevel(parent)
    center_window(mat_window, parent)
    mat_window.title("Material Settings")
    
    listbox = Listbox(mat_window, width=50, height=10)
    listbox.pack(pady=10)
    refresh_listbox()
    
    Button(mat_window, text="Add", command=open_add_popup).pack(side="left", padx=10)
    Button(mat_window, text="Remove", command=remove_material).pack(side="right", padx=10)