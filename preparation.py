def open_preparation_sub():
    from tkinter import Toplevel, Label, Entry
    prep_window = Toplevel()
    prep_window.title("Preparation Settings")
    Label(prep_window, text="Model Preparation (HH:MM):").pack()
    Entry(prep_window).pack()
    Label(prep_window, text="Slicing (HH:MM):").pack()
    Entry(prep_window).pack()
    Label(prep_window, text="Material Change (HH:MM):").pack()
    Entry(prep_window).pack()
    Label(prep_window, text="Transfer and Starting (HH:MM):").pack()
    Entry(prep_window).pack()