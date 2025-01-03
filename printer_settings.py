def open_printer_settings():
    from tkinter import Toplevel, Label, Button, Listbox, Entry, END, messagebox

    # Sample data for printers (you can replace this with actual data)
    printers = [
        {"name": "Printer 1", "model": "XYZ Pro", "type": "FDM", "bed_size": "200x200x200 mm"},
        {"name": "Printer 2", "model": "ABC Plus", "type": "SLA", "bed_size": "100x100x150 mm"}
    ]

    def refresh_listbox():
        """Refresh the listbox with printer data."""
        listbox.delete(0, END)
        for printer in printers:
            listbox.insert(END, f"{printer['name']} - {printer['model']} - {printer['type']} - {printer['bed_size']}")

    def open_add_printer_popup():
        """Open a popup window to add a new printer."""
        add_printer_window = Toplevel()
        add_printer_window.title("Add Printer")

        # Input fields
        Label(add_printer_window, text="Printer Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        name_entry = Entry(add_printer_window, width=30)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(add_printer_window, text="Model:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        model_entry = Entry(add_printer_window, width=30)
        model_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(add_printer_window, text="Type:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        type_entry = Entry(add_printer_window, width=30)
        type_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(add_printer_window, text="Bed Size:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        bed_size_entry = Entry(add_printer_window, width=30)
        bed_size_entry.grid(row=3, column=1, padx=10, pady=5)

        def add_printer():
            """Add the printer to the list and close the popup."""
            name = name_entry.get().strip()
            model = model_entry.get().strip()
            p_type = type_entry.get().strip()
            bed_size = bed_size_entry.get().strip()

            if not name or not model or not p_type or not bed_size:
                messagebox.showwarning("Input Error", "All fields must be filled!")
                return

            printers.append({"name": name, "model": model, "type": p_type, "bed_size": bed_size})
            refresh_listbox()
            add_printer_window.destroy()

        Button(add_printer_window, text="Add Printer", command=add_printer).grid(row=4, column=0, columnspan=2, pady=10)

    def remove_printer():
        """Remove the selected printer from the list."""
        selected_index = listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "Please select a printer to remove!")
            return

        printers.pop(selected_index[0])
        refresh_listbox()

    # Create the Printer Settings window
    printer_window = Toplevel()
    printer_window.title("Printer Settings")

    # List of Printers
    Label(printer_window, text="List of Printers:").pack(pady=5)
    listbox = Listbox(printer_window, width=60, height=10)
    listbox.pack(pady=5)
    refresh_listbox()

    # Buttons
    Button(printer_window, text="Add Printer", command=open_add_printer_popup).pack(pady=5)
    Button(printer_window, text="Remove Selected Printer", command=remove_printer).pack(pady=5)
