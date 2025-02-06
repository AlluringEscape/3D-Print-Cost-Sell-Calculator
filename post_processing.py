from tkinter import Toplevel, Label, Entry, Button
from utils import center_window

def open_post_processing_sub(parent, time_var):
    post_window = Toplevel(parent)
    center_window(post_window, parent)
    post_window.title("Post-Processing Settings")

    entries = {}
    tasks = [
        "Job Removal (HH:MM)",
        "Support Removal (HH:MM)",
        "Additional Work (HH:MM)"
    ]

    def save_time():
        total = sum(float(e.get().replace(":", ".")) for e in entries.values() if e.get())
        time_var.set(total)
        post_window.destroy()

    for i, task in enumerate(tasks):
        Label(post_window, text=task).grid(row=i, column=0, padx=5, pady=5)
        entries[task] = Entry(post_window)
        entries[task].grid(row=i, column=1, padx=5, pady=5)
    
    Button(post_window, text="Save", command=save_time).grid(row=len(tasks), columnspan=2)