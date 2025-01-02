from tkinter import *
from tkinter import ttk

# Initialize the main application window
root = Tk()
root.title("3D Printing Business Calculator")
root.geometry("600x400")

# Functions for opening submenus
def open_preparation_sub():
    prep_window = Toplevel(root)
    prep_window.title("Preparation Settings")
    Label(prep_window, text="Model Preparation (HH:MM):").pack()
    Entry(prep_window).pack()
    Label(prep_window, text="Slicing (HH:MM):").pack()
    Entry(prep_window).pack()
    Label(prep_window, text="Material Change (HH:MM):").pack()
    Entry(prep_window).pack()
    Label(prep_window, text="Transfer and Starting (HH:MM):").pack()
    Entry(prep_window).pack()

def open_post_processing_sub():
    post_window = Toplevel(root)
    post_window.title("Post-Processing Settings")
    Label(post_window, text="Job Removal (HH:MM):").pack()
    Entry(post_window).pack()
    Label(post_window, text="Support Removal (HH:MM):").pack()
    Entry(post_window).pack()
    Label(post_window, text="Additional Work (HH:MM):").pack()
    Entry(post_window).pack()

def open_consumable_sub():
    consum_window = Toplevel(root)
    consum_window.title("Consumables Settings")
    Button(consum_window, text="Open Consumables Settings", command=open_settings).pack()
    Label(consum_window, text="Select Consumables Used:").pack()
    # Example list of consumables
    consumables = ["Glue", "Tape", "Cleaning Alcohol"]
    for item in consumables:
        Checkbutton(consum_window, text=item).pack()

def open_settings():
    settings_window = Toplevel(root)
    settings_window.title("Settings")
    Label(settings_window, text="Main Settings: Energy Cost, Failure Rate, etc.").pack()
    Button(settings_window, text="Printer Settings", command=open_printer_settings).pack()
    Button(settings_window, text="Material Settings", command=open_material_settings).pack()

def open_printer_settings():
    printer_window = Toplevel(root)
    printer_window.title("Printer Settings")
    Label(printer_window, text="View/Add/Remove Printers").pack()

def open_material_settings():
    material_window = Toplevel(root)
    material_window.title("Material Settings")
    Label(material_window, text="View/Add/Remove Materials").pack()

# Main page widgets
Label(root, text="Printer:").grid(row=0, column=0, sticky=W)
printer_dropdown = ttk.Combobox(root, values=["Printer 1", "Printer 2"])
printer_dropdown.grid(row=0, column=1)
Button(root, text="Printer Settings", command=open_printer_settings).grid(row=0, column=2)

Label(root, text="Materials:").grid(row=1, column=0, sticky=W)
material_dropdown = ttk.Combobox(root, values=["Material 1", "Material 2"])
material_dropdown.grid(row=1, column=1)
Button(root, text="Material Settings", command=open_material_settings).grid(row=1, column=2)

Label(root, text="Weight (grams):").grid(row=2, column=0, sticky=W)
Entry(root).grid(row=2, column=1)

Label(root, text="Print Time (DD:HH:MM):").grid(row=3, column=0, sticky=W)
Entry(root).grid(row=3, column=1)

Button(root, text="Preparation", command=open_preparation_sub).grid(row=4, column=0, sticky=W)
Button(root, text="Post-Processing", command=open_post_processing_sub).grid(row=5, column=0, sticky=W)
Button(root, text="Consumables", command=open_consumable_sub).grid(row=6, column=0, sticky=W)

Button(root, text="Cost Breakdown", command=lambda: print("Open cost breakdown menu.")).grid(row=7, column=0, sticky=W)
Button(root, text="Generate Quote", command=lambda: print("Generate Quote Page.")).grid(row=8, column=0, sticky=W)

Button(root, text="Settings", command=open_settings).grid(row=9, column=0, sticky=W)

# Run the application
root.mainloop()
