from tkinter import Toplevel, Label, Button, Listbox, Entry, END, messagebox, ttk
from utils import load_data, save_data, MATERIALS_FILE, center_window

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

        Label(add_window, text="Total Cost ($):").grid(row=2, column=0, padx=5, pady=5)
        total_cost_entry = Entry(add_window)
        total_cost_entry.grid(row=2, column=1, padx=5, pady=5)

        Label(add_window, text="Total Material (grams):").grid(row=3, column=0, padx=5, pady=5)
        total_material_entry = Entry(add_window)
        total_material_entry.grid(row=3, column=1, padx=5, pady=5)

        Label(add_window, text="Cost per Gram ($/g):").grid(row=4, column=0, padx=5, pady=5)
        cost_per_gram_entry = Entry(add_window, state="readonly")
        cost_per_gram_entry.grid(row=4, column=1, padx=5, pady=5)

        def calculate_cost_per_gram(event=None):
            try:
                total_cost_text = total_cost_entry.get().strip()
                total_material_text = total_material_entry.get().strip()

                # Check if both fields have a valid input
                if not total_cost_text or not total_material_text:
                    cost_per_gram_entry.config(state="normal")
                    cost_per_gram_entry.delete(0, END)
                    cost_per_gram_entry.insert(0, "0.0000")
                    cost_per_gram_entry.config(state="readonly")
                    return  # Don't proceed further if input is empty

                total_cost = float(total_cost_text)
                total_material = float(total_material_text)

                if total_material > 0:
                    cost_per_gram = total_cost / total_material
                    cost_per_gram_entry.config(state="normal")
                    cost_per_gram_entry.delete(0, END)
                    cost_per_gram_entry.insert(0, f"{cost_per_gram:.4f}")
                    cost_per_gram_entry.config(state="readonly")
                else:
                    messagebox.showerror("Error", "Total Material must be greater than zero.")
            except ValueError:
                return  # Do nothing if the input is invalid, avoiding crashes

        # Bind event to recalculate when user enters values
        total_cost_entry.bind("<KeyRelease>", calculate_cost_per_gram)
        total_material_entry.bind("<KeyRelease>", calculate_cost_per_gram)

        def save_material():
            try:
                new_material = {
                    "brand": brand_entry.get().strip(),
                    "type": type_combo.get(),
                    "cost_per_gram": float(cost_per_gram_entry.get())
                }

                if not all(new_material.values()) or new_material["cost_per_gram"] == 0:
                    messagebox.showerror("Error", "All fields must be filled, and Cost/Gram must be greater than zero!")
                    return

                materials.append(new_material)
                save_data(materials, MATERIALS_FILE)
                refresh_listbox()
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid numeric values")

        Button(add_window, text="Save", command=save_material).grid(row=5, columnspan=2, pady=10)

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
