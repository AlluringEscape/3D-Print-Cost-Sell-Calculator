from tkinter import *
from tkinter import ttk
from preparation import open_preparation_sub
from post_processing import open_post_processing_sub
from consumables import open_consumable_sub
from printer_settings import open_printer_settings
from material_settings import open_material_settings
from settings import open_settings
from utils import load_data, load_settings, PRINTERS_FILE, MATERIALS_FILE, center_window
from calculator import calculate_cost

# Initialize main window
root = Tk()
root.title("3D Print Cost Calculator")
root.geometry("800x600")

# Variables
weight_var = DoubleVar()
print_time_var = DoubleVar()
preparation_time_var = DoubleVar(value=0.0)
post_processing_time_var = DoubleVar(value=0.0)
consumables_var = DoubleVar(value=0.0)

# ===== Printer Section =====
Label(root, text="Printer:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
printer_dropdown = ttk.Combobox(root, state="readonly")
printer_dropdown.grid(row=0, column=1, padx=5, pady=5)
Button(root, text="Manage Printers", 
      command=lambda: open_printer_settings(root, refresh_printer_dropdown)).grid(row=0, column=2)

# ===== Material Section =====
Label(root, text="Material:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
material_dropdown = ttk.Combobox(root, state="readonly")
material_dropdown.grid(row=1, column=1, padx=5, pady=5)
Button(root, text="Manage Materials", 
      command=lambda: open_material_settings(root)).grid(row=1, column=2)

# ===== Input Fields =====
Label(root, text="Weight (grams):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
Entry(root, textvariable=weight_var).grid(row=2, column=1, padx=5, pady=5)

Label(root, text="Print Time (hours):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
Entry(root, textvariable=print_time_var).grid(row=3, column=1, padx=5, pady=5)

# ===== Process Buttons =====
Button(root, text="Set Preparation Time", 
      command=lambda: open_preparation_sub(root, preparation_time_var)).grid(row=4, column=0, padx=10)
Button(root, text="Set Post-Processing Time", 
      command=lambda: open_post_processing_sub(root, post_processing_time_var)).grid(row=5, column=0, padx=10)
Button(root, text="Select Consumables", 
      command=lambda: open_consumable_sub(root, consumables_var)).grid(row=6, column=0, padx=10)

# ===== Refresh Functions =====
def refresh_printer_dropdown():
    printers = load_data(PRINTERS_FILE)
    printer_dropdown["values"] = [f"{p['name']} ({p['type']})" for p in printers]
    printer_dropdown.current(0) if printers else None
    update_material_dropdown()

def update_material_dropdown(event=None):
    try:
        printer_type = "Resin" if "Resin" in printer_dropdown.get() else "FDM"
        materials = [m for m in load_data(MATERIALS_FILE) if m["type"].upper() == printer_type.upper()]
        material_dropdown["values"] = [f"{m['brand']} (${m['cost_per_gram']}/g)" for m in materials]
        material_dropdown.current(0) if materials else None
    except:
        pass

printer_dropdown.bind("<<ComboboxSelected>>", update_material_dropdown)

# ===== Quote Generation =====
def show_quote():
    try:
        settings = load_settings()
        selected_material = next(m for m in load_data(MATERIALS_FILE) 
                               if m["brand"] in material_dropdown.get())
        
        breakdown = calculate_cost(
            material_cost=selected_material["cost_per_gram"],
            material_used=weight_var.get(),
            energy_cost=settings["energy_cost"],
            preparation_time=preparation_time_var.get(),
            labor_cost=settings["labor_cost"],
            fail_rate=settings["fail_rate"]/100,
            post_processing_time=post_processing_time_var.get(),
            consumables=consumables_var.get(),
            markup=settings["markup"]
        )

        # Create quote window
        quote_window = Toplevel(root)
        center_window(quote_window, root)
        quote_window.title("Cost Breakdown")
        
        # Format breakdown
        row = 0
        for key, value in breakdown.items():
            if key == "Total Cost": continue
            Label(quote_window, text=f"{key}:").grid(row=row, column=0, sticky="e", padx=10)
            Label(quote_window, text=f"${value:.2f}").grid(row=row, column=1, sticky="w")
            row += 1
        
        # Total
        Label(quote_window, text="Total Cost:", font=("Arial", 12, "bold")).grid(row=row, column=0, sticky="e")
        Label(quote_window, text=f"${breakdown['Total Cost']:.2f}", 
             font=("Arial", 12, "bold")).grid(row=row, column=1, sticky="w")
        
    except Exception as e:
        messagebox.showerror("Error", f"Missing data: {str(e)}")

Button(root, text="Generate Quote", command=show_quote).grid(row=7, column=0, pady=20)
Button(root, text="Settings", command=lambda: open_settings(root)).grid(row=8, column=0)

# Initialize
refresh_printer_dropdown()
root.mainloop()