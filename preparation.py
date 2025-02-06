from tkinter import Toplevel, Label, Entry, Button
from utils import *

def open_preparation_sub(parent, time_var):
    prep_window = Toplevel(parent)
    center_window(prep_window, parent)
    prep_window.title("Preparation Time")
    
    Label(prep_window, text="Enter Preparation Time:").pack(pady=5)
    time_entry = Entry(prep_window)
    time_entry.insert(0, "00:00")
    time_entry.pack()
    
    def save_time():
        hours = format_time_input(time_entry)
        time_var.set(hours)
        prep_window.destroy()
    
    Button(prep_window, text="Save", command=save_time).pack(pady=10)