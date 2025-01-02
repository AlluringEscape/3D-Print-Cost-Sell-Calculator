from tkinter import *
from tkinter import ttk
from preparation import open_preparation_sub
from post_processing import open_post_processing_sub
from consumables import open_consumables_sub
from settings import open_settings, open_printer_settings, open_material_settings


#Initalize the main app window
root = Tk()
root.title("3D Print Cost/Sell Calculator")
root.geometry("1600x1400")

#Main Page widgets

#Printer
Label(root, text="Printer:").grid(row=0, column=0, sticky=W)
printer_dropdown = ttk.Combobox(root, values=["Printer 1","Printer 2"])
printer_dropdown.grid(row=0,    column=1)
Button(root, text="Printer settings", command=open_printer_settings).gird(row=0, column=2)

#
