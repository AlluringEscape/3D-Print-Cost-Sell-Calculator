from tkinter import Toplevel, Label, Button, Listbox, Entry, END, messagebox, ttk
from utils import load_data, save_data, MATERIALS_FILE, center_window

def open_material_settings(parent):
    materials = load_data(MATERIALS_FILE)
    
    def refresh_listbox():
        listbox.delete(0, END)
        for mat in materials:
            listbox.insert(END, f"{mat['brand']} | {mat['type']} | ${mat['cost_per_gram']}/g")

    def open_add_material_popup():
        add_window = Toplevel(parent)
        center_window(add_window, parent)
        add_window.title("Add Material")
        
        fields = [
            ("Brand:", "text"),
            ("Type (FDM/Resin):", "text"),
            ("Cost per Gram ($):", "number"),
            ("Cost per Unit ($):", "number")
        ]
        
        entries = {}
        for i, (label, dtype) in enumerate(fields):
            Label(add_window, text=label).grid(row=i, column=0, padx=5, pady=5)
            entries[label] = Entry(add_window)
            entries[label].grid(row=i, column=1, padx=5, pady=5)
        
        def validate_and_add():
            try:
                new_mat = {
                    "brand": entries["Brand:"].get(),
                    "type": entries["Type (FDM/Resin):"].get().capitalize(),
                    "cost_per_gram": float(entries["Cost per Gram ($):"].get()),
                    "cost_per_unit": float(entries["Cost per Unit ($):"].get())
                }
                
                if new_mat["type"] not in ["Fdm", "Resin"]:
                    raise ValueError("Type must be FDM or Resin")
                
                materials.append(new_mat)
                save_data(materials, MATERIALS_FILE)
                refresh_listbox()
                add_window.destroy()
                
            except ValueError as e:
                messagebox.showerror("Input Error", f"Invalid format: {str(e)}")

        Button(add_window, text="Add", command=validate_and_add).grid(row=len(fields), columnspan=2)

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
    
    Button(mat_window, text="Add Material", command=open_add_material_popup).pack(side="left", padx=10)
    Button(mat_window, text="Remove Selected", command=remove_material).pack(side="right", padx=10)