from settings import open_settings

def open_consumable_sub():
    from tkinter import Toplevel, Label, Checkbutton, Button
    consum_window = Toplevel()
    consum_window.title("Consumables Settings")
    Button(consum_window, text="Open Consumables Settings", command=open_settings).pack()
    Label(consum_window, text="Select Consumables Used:").pack()
    consumables = ["Glue", "Tape", "Cleaning Alcohol"]
    for item in consumables:
        Checkbutton(consum_window, text=item).pack()