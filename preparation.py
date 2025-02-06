from tkinter import Toplevel, Label, Entry, Button
from utils import center_window

def open_preparation_sub(parent, time_var):
    prep_window = Toplevel(parent)
    prep_window.title("Preparation Settings")
    center_window(prep_window, parent)

    entries = {}
    tasks = [
        "Model Preparation (HH:MM)",
        "Slicing (HH:MM)",
        "Material Change (HH:MM)",
        "Transfer and Starting (HH:MM)"
    ]

    def save_time():
        total = sum(float(e.get().replace(":", ".")) for e in entries.values() if e.get())
        time_var.set(total)
        prep_window.destroy()

    for i, task in enumerate(tasks):
        Label(prep_window, text=task).grid(row=i, column=0, padx=5, pady=5)
        entries[task] = Entry(prep_window)
        entries[task].grid(row=i, column=1, padx=5, pady=5)
    
    Button(prep_window, text="Save", command=save_time).grid(row=len(tasks), columnspan=2)