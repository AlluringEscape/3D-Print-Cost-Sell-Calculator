from tkinter import Toplevel, Label, Button, Listbox, Entry, END, messagebox, ttk
from utils import *

PRINTER_DATABASE = [
    {"model": "Creality Ender 3", "type": "FDM", "bed_size": "220x220x250mm"},
    {"model": "Prusa i3 MK3S+", "type": "FDM", "bed_size": "250x210x210mm"},
    {"model": "Formlabs Form 3", "type": "SLA", "bed_size": "145x145x185mm"}
]

def open_printer_settings(parent, refresh_callback):
    printers = load_data(PRINTERS_FILE)
    
    def refresh_listbox():
        listbox.delete(0, END)
        for printer in printers:
            listbox.insert(END, f"{printer['name']} | {printer['model']} | {printer['bed_size']}")

    def open_add_printer_popup():
        add_window = Toplevel(parent)
        center_window(add_window, parent)
        add_window.title("Add Printer")
        
        # Input fields
        Label(add_window, text="Custom Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = Entry(add_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        Label(add_window, text="Select Model:").grid(row=1, column=0, padx=5, pady=5)
        model_combo = ttk.Combobox(add_window, values=[p["model"] for p in PRINTER_DATABASE])
        model_combo.grid(row=1, column=1, padx=5, pady=5)
        
        # Auto-fill details when model selected
        def model_selected(event):
            selected_model = next(p for p in PRINTER_DATABASE if p["model"] == model_combo.get())
            type_entry.delete(0, END)
            type_entry.insert(0, selected_model["type"])
            bed_size_entry.delete(0, END)
            bed_size_entry.insert(0, selected_model["bed_size"])
        
        model_combo.bind("<<ComboboxSelected>>", model_selected)
        
        Label(add_window, text="Type:").grid(row=2, column=0, padx=5, pady=5)
        type_entry = Entry(add_window)
        type_entry.grid(row=2, column=1, padx=5, pady=5)
        
        Label(add_window, text="Bed Size:").grid(row=3, column=0, padx=5, pady=5)
        bed_size_entry = Entry(add_window)
        bed_size_entry.grid(row=3, column=1, padx=5, pady=5)

        def save_printer():
            new_printer = {
                "name": name_entry.get(),
                "model": model_combo.get(),
                "type": type_entry.get(),
                "bed_size": bed_size_entry.get()
            }
            
            if not all(new_printer.values()):
                messagebox.showerror("Error", "All fields must be filled!")
                return
                
            printers.append(new_printer)
            save_data(printers, PRINTERS_FILE)
            refresh_listbox()
            refresh_callback()
            add_window.destroy()

        Button(add_window, text="Save", command=save_printer).grid(row=4, columnspan=2)

    def remove_printer():
        selected = listbox.curselection()
        if selected:
            printers.pop(selected[0])
            save_data(printers, PRINTERS_FILE)
            refresh_listbox()
            refresh_callback()

    printer_window = Toplevel(parent)
    center_window(printer_window, parent)
    printer_window.title("Printer Settings")
    
    listbox = Listbox(printer_window, width=70, height=10)
    listbox.pack(pady=10)
    refresh_listbox()
    
    Button(printer_window, text="Add Printer", command=open_add_printer_popup).pack(side="left", padx=10)
    Button(printer_window, text="Remove Selected", command=remove_printer).pack(side="right", padx=10)