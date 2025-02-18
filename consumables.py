from tkinter import Toplevel, Checkbutton, IntVar, Button
from utils import load_data, CONSUMABLES_FILE, center_window
from consumable_settings import open_consumable_settings

def open_consumable_sub(parent, cost_var):
    cons_window = Toplevel(parent)
    center_window(cons_window, parent)
    cons_window.title("Select Consumables")
    
    consumables = load_data(CONSUMABLES_FILE)
    vars = {}
    
    for i, cons in enumerate(consumables):
        vars[cons['name']] = IntVar()
        Checkbutton(cons_window, 
                    text=f"{cons['name']} (${cons['cost']})",
                    variable=vars[cons['name']]
                   ).pack(anchor="w", padx=20, pady=2)
    
    def save_selection():
        total = sum(cons['cost'] for cons in consumables if vars[cons['name']].get())
        cost_var.set(total)
        cons_window.destroy()
    
    Button(cons_window, text="Save", command=save_selection).pack(pady=10)
    Button(cons_window, text="Edit Consumables", command=lambda: open_consumable_settings(parent)).pack(pady=5)
