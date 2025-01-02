def open_settings():
    from tkinter import Toplevel, Label, Button
    settings_window = Toplevel()
    settings_window.title("Settings")
    Label(settings_window, text="Main Settings: Energy Cost, Failure Rate, etc.").pack()
    Button(settings_window, text="Printer Settings", command=open_printer_settings).pack()
    Button(settings_window, text="Material Settings", command=open_material_settings).pack()

def open_printer_settings():
    from tkinter import Toplevel, Label
    printer_window = Toplevel()
    printer_window.title("Printer Settings")
    Label(printer_window, text="View/Add/Remove Printers").pack()

def open_material_settings():
    from tkinter import Toplevel, Label
    material_window = Toplevel()
    material_window.title("Material Settings")
    Label(material_window, text="View/Add/Remove Materials").pack()
