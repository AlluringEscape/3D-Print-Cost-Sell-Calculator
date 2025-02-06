from tkinter import Toplevel, Label, Button, Entry, ttk
from utils import *

def open_settings(parent):
    settings_window = Toplevel(parent)
    center_window(settings_window, parent)
    settings_window.title("Application Settings")
    
    current = load_settings()
    entries = {}
    
    # Main Settings
    fields = [
        ("Hourly Energy Cost ($):", "energy_cost"),
        ("Hourly Labor Cost ($):", "labor_cost"),
        ("Failure Rate (%):", "fail_rate"),
        ("Markup (%):", "markup")
    ]
    
    for i, (label, key) in enumerate(fields):
        Label(settings_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entries[key] = Entry(settings_window)
        entries[key].insert(0, str(current[key]))
        entries[key].grid(row=i, column=1, padx=10, pady=5)
    
    # Other Settings Buttons
    Button(settings_window, text="Printer Settings",
          command=lambda: open_printer_settings(parent, lambda: None)).grid(row=4, columnspan=2)
    Button(settings_window, text="Material Settings",
          command=lambda: open_material_settings(parent)).grid(row=5, columnspan=2)
    Button(settings_window, text="Consumable Settings",
          command=lambda: open_consumable_settings(parent)).grid(row=6, columnspan=2)

    def save_settings():
        new_settings = {}
        try:
            new_settings["energy_cost"] = float(entries["energy_cost"].get())
            new_settings["labor_cost"] = float(entries["labor_cost"].get())
            new_settings["fail_rate"] = float(entries["fail_rate"].get())
            new_settings["markup"] = float(entries["markup"].get())
            save_data(new_settings, SETTINGS_FILE)
            settings_window.destroy()
        except:
            messagebox.showerror("Error", "Invalid numeric values")

    Button(settings_window, text="Save", command=save_settings).grid(row=7, columnspan=2)