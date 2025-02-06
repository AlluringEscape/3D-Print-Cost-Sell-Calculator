from tkinter import Toplevel, Label, Button, Listbox, Entry, END, messagebox
from utils import load_data, save_data, PRINTERS_FILE

def open_printer_settings(parent):
    printers = load_data(PRINTERS_FILE)
    
    def refresh_listbox():
        listbox.delete(0, END)
        for printer in printers:
            listbox.insert(END, f"{printer['name']} - {printer['model']} - {printer['type']} - {printer['bed_size']}")
    
    def open_add_printer_popup():
        add_window = Toplevel(parent)
        add_window.title("Add Printer")
        
        Label(add_window, text="Printer Name:").grid(row=0, column=0)
        name_entry = Entry(add_window)
        name_entry.grid(row=0, column=1)
        
        Label(add_window, text="Model:").grid(row=1, column=0)
        model_entry = Entry(add_window)
        model_entry.grid(row=1, column=1)
        
        Label(add_window, text="Type:").grid(row=2, column=0)
        type_entry = Entry(add_window)
        type_entry.grid(row=2, column=1)
        
        Label(add_window, text="Bed Size:").grid(row=3, column=0)
        bed_size_entry = Entry(add_window)
        bed_size_entry.grid(row=3, column=1)
        
        def add_printer():
            printers.append({
                "name": name_entry.get(),
                "model": model_entry.get(),
                "type": type_entry.get(),
                "bed_size": bed_size_entry.get()
            })
            save_data(printers, PRINTERS_FILE)
            refresh_listbox()
            add_window.destroy()
        
        Button(add_window, text="Add", command=add_printer).grid(row=4, columnspan=2)
    
    def remove_printer():
        selected = listbox.curselection()
        if selected:
            printers.pop(selected[0])
            save_data(printers, PRINTERS_FILE)
            refresh_listbox()
    
    printer_window = Toplevel(parent)
    printer_window.title("Printer Settings")
    
    listbox = Listbox(printer_window, width=60)
    listbox.pack()
    refresh_listbox()
    
    Button(printer_window, text="Add Printer", command=open_add_printer_popup).pack()
    Button(printer_window, text="Remove Selected", command=remove_printer).pack()