from tkinter import Toplevel, Label, Button, Listbox, Entry, END, messagebox, ttk
from utils import load_data, save_data, PRINTERS_FILE

# Global printer database
PRINTER_DATABASE = [
    {"model": "Creality Ender 3", "type": "FDM", "bed_size": "220x220x250mm"},
    {"model": "Prusa i3 MK3S+", "type": "FDM", "bed_size": "250x210x210mm"},
    {"model": "Formlabs Form 3", "type": "SLA", "bed_size": "145x145x185mm"}
]

def center_window(window, parent):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = parent.winfo_x() + (parent.winfo_width() // 2) - (width // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (height // 2)
    window.geometry(f'+{x}+{y}')

def open_printer_settings(parent, refresh_callback):
    printers = load_data(PRINTERS_FILE)
    
    def refresh_listbox():
        listbox.delete(0, END)
        for printer in printers:
            listbox.insert(END, f"{printer['name']} | {printer['model']} | {printer['type']} | {printer['bed_size']}")
        if refresh_callback:
            refresh_callback()

    def open_add_printer_popup():
        add_window = Toplevel(parent)
        add_window.title("Add Printer")
        center_window(add_window, parent)
        
        # Input fields
        Label(add_window, text="Custom Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = Entry(add_window, width=25)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        Label(add_window, text="Select Model:").grid(row=1, column=0, padx=5, pady=5)
        model_combobox = ttk.Combobox(add_window, values=[p["model"] for p in PRINTER_DATABASE], width=22)
        model_combobox.grid(row=1, column=1, padx=5, pady=5)
        model_combobox.set("Select or type custom")
        
        Label(add_window, text="Printer Type:").grid(row=2, column=0, padx=5, pady=5)
        type_entry = Entry(add_window, width=25)
        type_entry.grid(row=2, column=1, padx=5, pady=5)
        
        Label(add_window, text="Bed Size:").grid(row=3, column=0, padx=5, pady=5)
        bed_size_entry = Entry(add_window, width=25)
        bed_size_entry.grid(row=3, column=1, padx=5, pady=5)

        def model_selected(event):
            selected = model_combobox.get()
            if selected in [p["model"] for p in PRINTER_DATABASE]:
                printer = next(p for p in PRINTER_DATABASE if p["model"] == selected)
                type_entry.delete(0, END)
                type_entry.insert(0, printer["type"])
                bed_size_entry.delete(0, END)
                bed_size_entry.insert(0, printer["bed_size"])

        model_combobox.bind("<<ComboboxSelected>>", model_selected)

        def add_printer():
            new_printer = {
                "name": name_entry.get().strip(),
                "model": model_combobox.get().strip(),
                "type": type_entry.get().strip(),
                "bed_size": bed_size_entry.get().strip()
            }
            
            if not all(new_printer.values()):
                messagebox.showwarning("Error", "All fields must be filled!")
                return
                
            printers.append(new_printer)
            save_data(printers, PRINTERS_FILE)
            refresh_listbox()
            add_window.destroy()

        Button(add_window, text="Add Printer", command=add_printer).grid(row=4, columnspan=2, pady=10)

    def remove_printer():
        selected = listbox.curselection()
        if selected:
            printers.pop(selected[0])
            save_data(printers, PRINTERS_FILE)
            refresh_listbox()

    printer_window = Toplevel(parent)
    printer_window.title("Printer Settings")
    center_window(printer_window, parent)
    
    listbox = Listbox(printer_window, width=70, height=10)
    listbox.pack(pady=10)
    refresh_listbox()
    
    Button(printer_window, text="Add Printer", command=open_add_printer_popup).pack(side="left", padx=10)
    Button(printer_window, text="Remove Selected", command=remove_printer).pack(side="right", padx=10)