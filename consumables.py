from tkinter import Toplevel, Label, Checkbutton, IntVar, Button
from utils import center_window

CONSUMABLE_COSTS = {
    "Glue": 5,
    "Tape": 3,
    "Cleaning Alcohol": 8
}

def open_consumable_sub(parent, cost_var):
    consum_window = Toplevel(parent)
    consum_window.title("Consumables")
    center_window(consum_window, parent)
    
    selected = {}
    for item in CONSUMABLE_COSTS:
        var = IntVar()
        Checkbutton(consum_window, text=f"{item} (${CONSUMABLE_COSTS[item]})", variable=var).pack(pady=2)
        selected[item] = var

    def save_costs():
        total = sum(CONSUMABLE_COSTS[item] for item, var in selected.items() if var.get())
        cost_var.set(total)
        consum_window.destroy()

    Button(consum_window, text="Save", command=save_costs).pack(pady=10)