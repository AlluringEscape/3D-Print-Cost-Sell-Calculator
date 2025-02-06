from tkinter import Toplevel, Label, Button, Entry
from utils import load_settings, save_data, SETTINGS_FILE
from printer_settings import open_printer_settings
from material_settings import open_material_settings

def open_settings(parent):
    settings_window = Toplevel(parent)
    settings_window.title("Settings")
    
    current = load_settings()
    
    entries = {}
    for i, (key, val) in enumerate(current.items()):
        Label(settings_window, text=f"{key.replace('_', ' ').title()}:").grid(row=i, column=0)
        entries[key] = Entry(settings_window)
        entries[key].insert(0, str(val))
        entries[key].grid(row=i, column=1)
    
    def save():
        new_settings = {k: float(v.get()) for k, v in entries.items()}
        save_data(new_settings, SETTINGS_FILE)
        settings_window.destroy()
    
    Button(settings_window, text="Save", command=save).grid(row=len(current)+1, columnspan=2)
    Button(settings_window, text="Printer Settings", command=lambda: open_printer_settings(parent)).pack()
    Button(settings_window, text="Material Settings", command=lambda: open_material_settings(parent)).pack()