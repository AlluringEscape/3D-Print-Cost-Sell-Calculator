from tkinter import Toplevel, Label, Entry, Button
from utils import center_window, format_time_input

def open_post_processing_sub(parent, job_removal_var, support_removal_var, additional_work_var):
    post_window = Toplevel(parent)
    center_window(post_window, parent)
    post_window.title("Post-Processing Time")
    
    labels = [
        "Job Removal",
        "Support Removal",
        "Additional Work (sanding, Painting...)"
    ]
    entries = {}
    
    for i, text in enumerate(labels):
        Label(post_window, text=text).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = Entry(post_window)
        entry.insert(0, "00:00")
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[text] = entry
        
    def save_times():
        job_hours = format_time_input(entries["Job Removal"])
        support_hours = format_time_input(entries["Support Removal"])
        additional_hours = format_time_input(entries["Additional Work (sanding, Painting...)"])
        
        job_removal_var.set(job_hours)
        support_removal_var.set(support_hours)
        additional_work_var.set(additional_hours)
        post_window.destroy()
        
    Button(post_window, text="Save", command=save_times).grid(row=len(labels), columnspan=2, pady=10)
