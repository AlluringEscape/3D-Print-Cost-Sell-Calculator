import tkinter as tk
from tkinter import ttk

# Global settings (modifiable in settings menu)
settings = {
    "energy_cost": 0.3,
    "labor_cost": 10,
    "failure_rate": 10,
    "markup": 150
}

printers = ["Printer A", "Printer B", "Printer C"]
materials = ["PLA", "ABS", "Resin"]
consumables = ["Glue Stick", "Painter's Tape", "Alcohol Wipes"]

def open_settings_menu():
    def save_settings():
        try:
            settings["energy_cost"] = float(energy_cost_var.get())
            settings["labor_cost"] = float(labor_cost_var.get())
            settings["failure_rate"] = float(failure_rate_var.get())
            settings["markup"] = float(markup_var.get())
            settings_window.destroy()
        except ValueError:
            settings_error.set("Please enter valid numbers.")

    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    energy_cost_var.set(settings["energy_cost"])
    labor_cost_var.set(settings["labor_cost"])
    failure_rate_var.set(settings["failure_rate"])
    markup_var.set(settings["markup"])

    ttk.Label(settings_window, text="Energy Cost per Hour ($):").grid(column=0, row=0, padx=10, pady=5, sticky="W")
    ttk.Entry(settings_window, textvariable=energy_cost_var).grid(column=1, row=0, padx=10, pady=5)

    ttk.Label(settings_window, text="Labor Cost per Hour ($):").grid(column=0, row=1, padx=10, pady=5, sticky="W")
    ttk.Entry(settings_window, textvariable=labor_cost_var).grid(column=1, row=1, padx=10, pady=5)

    ttk.Label(settings_window, text="Failure Rate (%):").grid(column=0, row=2, padx=10, pady=5, sticky="W")
    ttk.Entry(settings_window, textvariable=failure_rate_var).grid(column=1, row=2, padx=10, pady=5)

    ttk.Label(settings_window, text="Markup Percentage (%):").grid(column=0, row=3, padx=10, pady=5, sticky="W")
    ttk.Entry(settings_window, textvariable=markup_var).grid(column=1, row=3, padx=10, pady=5)

    ttk.Button(settings_window, text="Save", command=save_settings).grid(column=0, row=4, columnspan=2, pady=10)
    settings_error_label = ttk.Label(settings_window, textvariable=settings_error, foreground="red")
    settings_error_label.grid(column=0, row=5, columnspan=2)

def manage_printers():
    def add_printer():
        new_printer = printer_name_var.get()
        if new_printer and new_printer not in printers:
            printers.append(new_printer)
            printer_listbox.insert(tk.END, new_printer)

    def remove_printer():
        selected = printer_listbox.curselection()
        if selected:
            printers.pop(selected[0])
            printer_listbox.delete(selected)

    printer_window = tk.Toplevel(root)
    printer_window.title("Manage Printers")

    ttk.Label(printer_window, text="Printers:").grid(column=0, row=0, padx=10, pady=5)
    printer_listbox = tk.Listbox(printer_window)
    printer_listbox.grid(column=0, row=1, padx=10, pady=5)

    for printer in printers:
        printer_listbox.insert(tk.END, printer)

    ttk.Label(printer_window, text="Add Printer:").grid(column=1, row=0, padx=10, pady=5)
    printer_name_var = tk.StringVar()
    ttk.Entry(printer_window, textvariable=printer_name_var).grid(column=1, row=1, padx=10, pady=5)
    ttk.Button(printer_window, text="Add", command=add_printer).grid(column=1, row=2, padx=10, pady=5)

    ttk.Button(printer_window, text="Remove Selected", command=remove_printer).grid(column=0, row=2, padx=10, pady=5)

def manage_materials():
    def add_material():
        new_material = material_name_var.get()
        if new_material and new_material not in materials:
            materials.append(new_material)
            material_listbox.insert(tk.END, new_material)

    def remove_material():
        selected = material_listbox.curselection()
        if selected:
            materials.pop(selected[0])
            material_listbox.delete(selected)

    material_window = tk.Toplevel(root)
    material_window.title("Manage Materials")

    ttk.Label(material_window, text="Materials:").grid(column=0, row=0, padx=10, pady=5)
    material_listbox = tk.Listbox(material_window)
    material_listbox.grid(column=0, row=1, padx=10, pady=5)

    for material in materials:
        material_listbox.insert(tk.END, material)

    ttk.Label(material_window, text="Add Material:").grid(column=1, row=0, padx=10, pady=5)
    material_name_var = tk.StringVar()
    ttk.Entry(material_window, textvariable=material_name_var).grid(column=1, row=1, padx=10, pady=5)
    ttk.Button(material_window, text="Add", command=add_material).grid(column=1, row=2, padx=10, pady=5)

    ttk.Button(material_window, text="Remove Selected", command=remove_material).grid(column=0, row=2, padx=10, pady=5)

def manage_consumables():
    def add_consumable():
        new_consumable = consumable_name_var.get()
        if new_consumable and new_consumable not in consumables:
            consumables.append(new_consumable)
            consumable_listbox.insert(tk.END, new_consumable)

    def remove_consumable():
        selected = consumable_listbox.curselection()
        if selected:
            consumables.pop(selected[0])
            consumable_listbox.delete(selected)

    consumable_window = tk.Toplevel(root)
    consumable_window.title("Manage Consumables")

    ttk.Label(consumable_window, text="Consumables:").grid(column=0, row=0, padx=10, pady=5)
    consumable_listbox = tk.Listbox(consumable_window)
    consumable_listbox.grid(column=0, row=1, padx=10, pady=5)

    for consumable in consumables:
        consumable_listbox.insert(tk.END, consumable)

    ttk.Label(consumable_window, text="Add Consumable:").grid(column=1, row=0, padx=10, pady=5)
    consumable_name_var = tk.StringVar()
    ttk.Entry(consumable_window, textvariable=consumable_name_var).grid(column=1, row=1, padx=10, pady=5)
    ttk.Button(consumable_window, text="Add", command=add_consumable).grid(column=1, row=2, padx=10, pady=5)

    ttk.Button(consumable_window, text="Remove Selected", command=remove_consumable).grid(column=0, row=2, padx=10, pady=5)

root = tk.Tk()
root.title("3D Printing Business Calculator")

energy_cost_var = tk.StringVar()
labor_cost_var = tk.StringVar()
failure_rate_var = tk.StringVar()
markup_var = tk.StringVar()
settings_error = tk.StringVar()

# Main Menu Buttons
ttk.Button(root, text="Manage Printers", command=manage_printers).grid(column=0, row=0, padx=10, pady=5)
ttk.Button(root, text="Manage Materials", command=manage_materials).grid(column=0, row=1, padx=10, pady=5)
ttk.Button(root, text="Manage Consumables", command=manage_consumables).grid(column=0, row=2, padx=10, pady=5)
ttk.Button(root, text="Settings", command=open_settings_menu).grid(column=0, row=3, padx=10, pady=5)

root.mainloop()
