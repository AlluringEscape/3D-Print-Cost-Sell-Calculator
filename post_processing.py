def open_post_processing_sub():
    from tkinter import Toplevel, Label, Entry
    post_window = Toplevel()
    post_window.title("Post-Processing Settings")
    Label(post_window, text="Job Removal (HH:MM):").pack()
    Entry(post_window).pack()
    Label(post_window, text="Support Removal (HH:MM):").pack()
    Entry(post_window).pack()
    Label(post_window, text="Additional Work (HH:MM):").pack()
    Entry(post_window).pack()