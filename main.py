from tkinter import *
from tkinter import ttk
from preparation import open_preparation_sub
from post_processing import open_post_processing_sub
from consumables import open_consumable_sub
from printer_settings import open_printer_settings
from material_settings import open_material_settings
from settings import open_settings
from utils import load_settings
from calculator import calculate_cost

root = Tk()
root.title("3D Print Cost/Sell Calculator")
root.geometry("600x400")

# Variables
weight_var = DoubleVar()
print_time_var = DoubleVar()
preparation_time_var = DoubleVar(value=0)  # New
post_processing_time_var = DoubleVar(value=0)  # New
consumables_cost_var = DoubleVar(value=0)  # New

# Printer
Label(root, text="Printer:").grid(row=0, column=0, sticky=W)
printer_dropdown = ttk.Combobox(root)
printer_dropdown.grid(row=0, column=1)
Button(root, text="Printer Settings", command=lambda: open_printer_settings(root, refresh_printer_dropdown)).grid(row=0, column=2)

# Materials
Label(root, text="Materials:").grid(row=1, column=0, sticky=W)
material_dropdown = ttk.Combobox(root)
material_dropdown.grid(row=1, column=1)
Button(root, text="Material Settings", command=lambda: open_material_settings(root)).grid(row=1, column=2)

# Weight
Label(root, text="Weight (Grams):").grid(row=2, column=0, sticky=W)
Entry(root, textvariable=weight_var).grid(row=2, column=1)

# Print Time
Label(root, text="Print Time (Hours):").grid(row=3, column=0, sticky=W)
Entry(root, textvariable=print_time_var).grid(row=3, column=1)

# Buttons
Button(root, text="Preparation", command=lambda: open_preparation_sub(root, preparation_time_var)).grid(row=4, column=0, sticky=W)
Button(root, text="Post-Processing", command=lambda: open_post_processing_sub(root, post_processing_time_var)).grid(row=5, column=0, sticky=W)
Button(root, text="Consumables", command=lambda: open_consumable_sub(root, consumables_cost_var)).grid(row=6, column=0, sticky=W)
Button(root, text="Settings", command=lambda: open_settings(root)).grid(row=9, column=0, sticky=W)

def refresh_printer_dropdown():
    printers = load_data(PRINTERS_FILE)
    printer_dropdown['values'] = [f"{p['name']} ({p['model']})" for p in printers]
    if printers:
        printer_dropdown.current(0)

def show_quote():
    settings = load_settings()
    total = calculate_cost(
        material_cost=10,  # Will connect to material dropdown later
        material_used=weight_var.get(),
        energy_cost=settings["energy_cost"],
        preparation_time=preparation_time_var.get(),
        labor_cost=settings["labor_cost"],
        fail_rate=settings["fail_rate"]/100,
        post_processing_time=post_processing_time_var.get(),
        consumables=consumables_cost_var.get(),
        markup=settings["markup"]
    )
    quote_window = Toplevel(root)
    Label(quote_window, text=f"Total Cost: ${total:.2f}").pack()

Button(root, text="Print Quote", command=show_quote).grid(row=8, column=0, sticky=W)

# Initialize
from utils import load_data, PRINTERS_FILE
refresh_printer_dropdown()
root.mainloop()