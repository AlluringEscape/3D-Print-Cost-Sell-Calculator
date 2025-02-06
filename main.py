from tkinter import *
from tkinter import ttk
from preparation import open_preparation_sub
from post_processing import open_post_processing_sub
from consumables import open_consumable_sub
from printer_settings import open_printer_settings
from material_settings import open_material_settings
from settings import open_settings
from utils import load_settings, load_data, PRINTERS_FILE, MATERIALS_FILE, center_window
from calculator import calculate_cost

# Initialize main window
root = Tk()
root.title("3D Print Cost/Sell Calculator")
root.geometry("800x600")

# Variables
weight_var = DoubleVar()
print_time_var = DoubleVar()
preparation_time_var = DoubleVar(value=0.0)
post_processing_time_var = DoubleVar(value=0.0)
consumables_cost_var = DoubleVar(value=0.0)

# ========== Printer Section ==========
Label(root, text="Printer:").grid(row=0, column=0, sticky=W, padx=10, pady=5)
printer_dropdown = ttk.Combobox(root, state="readonly", width=30)
printer_dropdown.grid(row=0, column=1, padx=5, pady=5)
Button(root, text="Printer Settings", 
      command=lambda: open_printer_settings(root, refresh_printer_dropdown)).grid(row=0, column=2, padx=5)

# ========== Material Section ==========
Label(root, text="Material:").grid(row=1, column=0, sticky=W, padx=10, pady=5)
material_dropdown = ttk.Combobox(root, state="readonly", width=30)
material_dropdown.grid(row=1, column=1, padx=5, pady=5)
Button(root, text="Material Settings", 
      command=lambda: open_material_settings(root)).grid(row=1, column=2, padx=5)

# ========== Weight/Time Inputs ==========
Label(root, text="Weight (grams):").grid(row=2, column=0, sticky=W, padx=10, pady=5)
Entry(root, textvariable=weight_var).grid(row=2, column=1, padx=5, pady=5)

Label(root, text="Print Time (hours):").grid(row=3, column=0, sticky=W, padx=10, pady=5)
Entry(root, textvariable=print_time_var).grid(row=3, column=1, padx=5, pady=5)

# ========== Process Buttons ==========
Button(root, text="Preparation", 
      command=lambda: open_preparation_sub(root, preparation_time_var)).grid(row=4, column=0, sticky=W, padx=10, pady=5)
Button(root, text="Post-Processing", 
      command=lambda: open_post_processing_sub(root, post_processing_time_var)).grid(row=5, column=0, sticky=W, padx=10, pady=5)
Button(root, text="Consumables", 
      command=lambda: open_consumable_sub(root, consumables_cost_var)).grid(row=6, column=0, sticky=W, padx=10, pady=5)

# ========== Refresh Functions ==========
def refresh_printer_dropdown():
    printers = load_data(PRINTERS_FILE)
    printer_dropdown['values'] = [f"{p['name']} ({p['type']})" for p in printers]
    if printers:
        printer_dropdown.current(0)
    update_material_dropdown()

def update_material_dropdown(event=None):
    try:
        printer_type = "Resin" if "Resin" in printer_dropdown.get() else "FDM"
        materials = [m for m in load_data(MATERIALS_FILE) if m['type'].lower() == printer_type.lower()]
        material_dropdown['values'] = [f"{m['brand']} (${m['cost_per_gram']}/g)" for m in materials]
        if materials:
            material_dropdown.current(0)
    except Exception as e:
        print(f"Error updating materials: {str(e)}")

# ========== Quote Generation ==========
def show_quote():
    try:
        settings = load_settings()
        
        # Get selected material
        material_str = material_dropdown.get()
        selected_material = next(m for m in load_data(MATERIALS_FILE) 
                               if f"{m['brand']} (${m['cost_per_gram']}/g)" == material_str)
        
        # Calculate costs
        cost_breakdown = calculate_cost(
            material_cost=selected_material['cost_per_gram'],
            material_used=weight_var.get(),
            energy_cost=settings["energy_cost"],
            preparation_time=preparation_time_var.get(),
            labor_cost=settings["labor_cost"],
            fail_rate=settings["fail_rate"]/100,
            post_processing_time=post_processing_time_var.get(),
            consumables=consumables_cost_var.get(),
            markup=settings["markup"]
        )

        # Create quote window
        quote_window = Toplevel(root)
        center_window(quote_window, root)
        quote_window.title("Cost Breakdown")
        
        # Breakdown labels
        Label(quote_window, text="Cost Breakdown", font=("Arial", 14, "bold")).grid(row=0, columnspan=2, pady=10)
        
        row_num = 1
        for key, value in cost_breakdown.items():
            if key == "Total": continue
            Label(quote_window, text=f"{key}:").grid(row=row_num, column=0, sticky="e", padx=5)
            Label(quote_window, text=f"${value:.2f}").grid(row=row_num, column=1, sticky="w", padx=10)
            row_num += 1
            
        Label(quote_window, text="Total Cost:", font=("Arial", 12, "bold")).grid(row=row_num, column=0, sticky="e", pady=10)
        Label(quote_window, text=f"${cost_breakdown['Total']:.2f}", 
             font=("Arial", 12, "bold")).grid(row=row_num, column=1, sticky="w")
            
    except Exception as e:
        error_window = Toplevel(root)
        center_window(error_window, root)
        Label(error_window, text=f"Error: {str(e)}", fg="red").pack(padx=20, pady=20)

# ========== Final Buttons ==========
Button(root, text="Print Quote", command=show_quote).grid(row=7, column=0, sticky=W, padx=10, pady=10)
Button(root, text="Settings", command=lambda: open_settings(root)).grid(row=8, column=0, sticky=W, padx=10, pady=5)

# Initialize dropdowns
printer_dropdown.bind("<<ComboboxSelected>>", update_material_dropdown)
refresh_printer_dropdown()

# Start application
root.mainloop()