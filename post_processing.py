from tkinter import Toplevel, Label, Entry, Button
from utils import *

def open_post_processing_sub(parent, time_var):
    post_window = Toplevel(parent)
    center_window(post_window, parent)
    post_window.title("Post-Processing Time")
    
    Label(post_window, text="Enter Post-Processing Time:").pack(pady=5)
    time_entry = Entry(post_window)
    time_entry.insert(0, "00:00")
    time_entry.pack()
    
    def save_time():
        hours = format_time_input(time_entry)
        time_var.set(hours)
        post_window.destroy()
    
    Button(post_window, text="Save", command=save_time).pack(pady=10)