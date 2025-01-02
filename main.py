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
printer_dropdown.grid(row=0, column=1)
Button(root, text="Printer settings", command=open_printer_settings).gird(row=0, column=2)

#Materials
Label(root, text="Materials:").grid(row=1, column=0,sticky=W)
material_dropdown= ttk.Combobox(root, values=["Material 1", "Material 2"])
material_dropdown.grid(row=1, column=1)
Button(root, text="Material Settings", command=open_material_settings).grid(row=1, column=2)

#Weight
Label(root, text="weight(Grams):").grid(row=2, column=0, sticky=W)
Entry(root).grid(row=2, column=1)

#Print Time
Label(root, text="Print Time:").grid(row=3, column=0, sticky=W)
Entry(root).grid(row=3, column=1)

#Preparation
Button(root, text="Preparation", command=open_preparation_sub).grid(row=4, column=0, sticky=W)

#Post-Processing
Button(root, text="Post-Processing", command=open_post_processing_sub).grid(row=5, column=0, sticky=W)

#Concumables
Button(root, text="Consumables", command=open_consumables_sub).grid(row=6, column=0, sticky=W)

#Cost Breakdown
Button(root, text="Cost Breakdown", command=lambda: print("Menu")).grid(row=7, column=0, sticky=W)

#Print Quote
Button(root, text="Print Qoute", command=lambda: print("Qoute")).grid(row=7, column=0, sticky=W)

#Setting
Button(root, text="Settings", command=open_settings).grid(row=9, column=0, sticky=W)

#run App
root.mainloop