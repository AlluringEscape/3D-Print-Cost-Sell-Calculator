from tkinter import *
from tkinter import ttk
from preparation import open_preparation_sub
from post_processing import open_post_processing_sub
from consumables import open_consumable_sub
from printer_settings import open_printer_settings
from settings import open_settings
from utils import load_settings
from utils import load_data, PRINTERS_FILE

root = Tk()
root.title("3D Print Cost/Sell Calculator")
root.geometry("600x400")

# Variables
weight_var = DoubleVar()
print_time_var = DoubleVar()

# Update the printer dropdown section
def refresh_printer_dropdown():
    printers = load_data(PRINTERS_FILE)
    printer_dropdown["values"] = [f"{p['name']} ({p['model']})" for p in printers]
    if printers:
        printer_dropdown.current(0)

# Printer 
Label(root, text="Printer:").grid(row=0, column=0, sticky=W)
printer_dropdown = ttk.Combobox(root)
printer_dropdown.grid(row=0, column=1)
Button(root, text="Printer Settings", command=lambda: open_printer_settings(root, refresh_printer_dropdown)).grid(row=0, column=2)

# Materials
Label(root, text="Materials:").grid(row=1, column=0, sticky=W)
material_dropdown = ttk.Combobox(root, values=["Material 1", "Material 2"])
material_dropdown.grid(row=1, column=1)
Button(root, text="Material Settings", command=lambda: open_material_settings(root)).grid(row=1, column=2)

# Weight
Label(root, text="Weight (Grams):").grid(row=2, column=0, sticky=W)
Entry(root, textvariable=weight_var).grid(row=2, column=1)

# Print Time
Label(root, text="Print Time (Hours):").grid(row=3, column=0, sticky=W)
Entry(root, textvariable=print_time_var).grid(row=3, column=1)

# Buttons
Button(root, text="Preparation", command=lambda: open_preparation_sub(root)).grid(row=4, column=0, sticky=W)
Button(root, text="Post-Processing", command=lambda: open_post_processing_sub(root)).grid(row=5, column=0, sticky=W)
Button(root, text="Consumables", command=lambda: open_consumable_sub(root)).grid(row=6, column=0, sticky=W)
Button(root, text="Settings", command=lambda: open_settings(root)).grid(row=9, column=0, sticky=W)

def show_quote():
    settings = load_settings()
    total = calculate_cost(
        material_cost=10,  # Placeholder
        material_used=weight_var.get(),
        energy_cost=settings["energy_cost"],
        preparation_time=1,  # Placeholder
        labor_cost=settings["labor_cost"],
        fail_rate=settings["fail_rate"]/100,
        post_processing_time=0.5,  # Placeholder
        consumables=5,  # Placeholder
        markup=settings["markup"]
    )
    quote_window = Toplevel(root)
    Label(quote_window, text=f"Total Cost: ${total:.2f}").pack()

Button(root, text="Print Quote", command=show_quote).grid(row=8, column=0, sticky=W)

refresh_printer_dropdown()

root.mainloop()