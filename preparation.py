from tkinter import Toplevel, Label, Entry, Button
from utils import center_window, format_time_input

def open_preparation_sub(parent, model_prep_var, slicing_var, material_change_var, transfer_var):
    prep_window = Toplevel(parent)
    center_window(prep_window, parent)
    prep_window.title("Preparation Time")
    
    labels = [
        "Model Preparation (Fixing, CAD...)",
        "Slicing (Supports, Parameters...)",
        "Material Change",
        "Transfer & Start"
    ]
    entries = {}
    
    for i, text in enumerate(labels):
        Label(prep_window, text=text).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = Entry(prep_window)
        entry.insert(0, "00:00")
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[text] = entry
        
    def save_times():
        # Parse each entry using the HH:MM format helper
        model_hours = format_time_input(entries["Model Preparation (Fixing, CAD...)"])
        slicing_hours = format_time_input(entries["Slicing (Supports, Parameters...)"])
        material_change_hours = format_time_input(entries["Material Change"])
        transfer_hours = format_time_input(entries["Transfer & Start"])
        
        model_prep_var.set(model_hours)
        slicing_var.set(slicing_hours)
        material_change_var.set(material_change_hours)
        transfer_var.set(transfer_hours)
        prep_window.destroy()
        
    Button(prep_window, text="Save", command=save_times).grid(row=len(labels), columnspan=2, pady=10)
