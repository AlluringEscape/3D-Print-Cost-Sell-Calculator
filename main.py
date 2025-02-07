from tkinter import *
from tkinter import ttk, messagebox
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

# Existing variables
weight_var = DoubleVar()
print_time_var = DoubleVar()
consumables_var = DoubleVar(value=0.0)

# New variables for Preparation components
model_prep_var = DoubleVar(value=0.0)
slicing_var = DoubleVar(value=0.0)
material_change_var = DoubleVar(value=0.0)
transfer_var = DoubleVar(value=0.0)

# New variables for Post-Processing components
job_removal_var = DoubleVar(value=0.0)
support_removal_var = DoubleVar(value=0.0)
additional_work_var = DoubleVar(value=0.0)

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
Button(root, text="Preparation", 
       command=lambda: open_preparation_sub(root, model_prep_var, slicing_var, material_change_var, transfer_var)
      ).grid(row=4, column=0, padx=10)

Button(root, text="Post-Processing", 
       command=lambda: open_post_processing_sub(root, job_removal_var, support_removal_var, additional_work_var)
      ).grid(row=5, column=0, padx=10)

Button(root, text="Select Consumables", 
       command=lambda: open_consumable_sub(root, consumables_var)
      ).grid(row=6, column=0, padx=10)
Button(root, text="Edit Consumables", 
       command=lambda: open_consumable_sub(root, consumables_var)  # Alternatively, directly call open_consumable_settings
      ).grid(row=6, column=1, padx=10)

# ===== Refresh Functions =====
def refresh_printer_dropdown():
    printers = load_data(PRINTERS_FILE)
    printer_dropdown["values"] = [f"{p['name']} ({p['type']})" for p in printers]
    if printers:
        printer_dropdown.current(0)
    update_material_dropdown()

def update_material_dropdown(event=None):
    try:
        printer_type = "Resin" if "Resin" in printer_dropdown.get() else "FDM"
        materials = [m for m in load_data(MATERIALS_FILE) if m["type"].upper() == printer_type.upper()]
        material_dropdown["values"] = [f"{m['brand']} (${m['cost_per_gram']}/g)" for m in materials]
        if materials:
            material_dropdown.current(0)
    except:
        pass

printer_dropdown.bind("<<ComboboxSelected>>", update_material_dropdown)

# ===== Quote Generation =====
def show_quote():
    try:
        settings = load_settings()
        selected_material = next(m for m in load_data(MATERIALS_FILE) 
                               if m["brand"] in material_dropdown.get())
        # Create dictionaries for the breakdown components:
        prep_components = {
            "model_preparation": model_prep_var.get(),
            "slicing": slicing_var.get(),
            "material_change": material_change_var.get(),
            "transfer": transfer_var.get()
        }
        post_components = {
            "job_removal": job_removal_var.get(),
            "support_removal": support_removal_var.get(),
            "additional_work": additional_work_var.get()
        }
        
        breakdown = calculate_cost(
            material_cost=selected_material["cost_per_gram"],
            material_used=weight_var.get(),
            print_time=print_time_var.get(),
            prep_components=prep_components,
            post_components=post_components,
            consumables=consumables_var.get(),
            energy_cost=settings["energy_cost"],
            labor_cost=settings["labor_cost"],
            fail_rate=settings["fail_rate"]/100,
            markup=settings["markup"]
        )
        
        # Create quote window to display the breakdown
        quote_window = Toplevel(root)
        center_window(quote_window, root)
        quote_window.title("Cost Breakdown")
        
        row = 0
        for key, value in breakdown.items():
            Label(quote_window, text=f"{key}:").grid(row=row, column=0, sticky="e", padx=10)
            Label(quote_window, text=f"${value:.2f}").grid(row=row, column=1, sticky="w")
            row += 1
        
    except Exception as e:
        messagebox.showerror("Error", f"Missing data: {str(e)}")

Button(root, text="Generate Quote", command=show_quote).grid(row=7, column=0, pady=20)
Button(root, text="Settings", command=lambda: open_settings(root)).grid(row=8, column=0)

# Initialize dropdown
refresh_printer_dropdown()
root.mainloop()
