import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_cost():
    try:
        # Get input values
        energy_cost = float(energy_cost_entry.get())
        labor_cost = float(labor_cost_entry.get())
        failure_rate = float(failure_rate_entry.get()) / 100
        material_cost = float(material_cost_entry.get())
        material_used = float(material_used_entry.get())
        prep_time = float(prep_time_entry.get())
        post_time = float(post_time_entry.get())
        consumables_cost = float(consumables_cost_entry.get())
        markup = float(markup_entry.get()) / 100

        # Calculate costs
        electricity_cost = energy_cost * (prep_time + post_time)
        labor_cost_total = labor_cost * (prep_time + post_time)
        material_total = material_cost * material_used
        failure_total = (electricity_cost + labor_cost_total + material_total + consumables_cost) * failure_rate
        base_cost = electricity_cost + labor_cost_total + material_total + consumables_cost + failure_total
        final_price = base_cost * (1 + markup)

        # Display result
        result_label.config(text=f"Total Cost: ${final_price:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("3D Printing Cost Calculator")
root.geometry("400x600")

# Create input fields
ttk.Label(root, text="Energy cost per hour ($):").pack()
energy_cost_entry = ttk.Entry(root)
energy_cost_entry.pack()

ttk.Label(root, text="Labor cost per hour ($):").pack()
labor_cost_entry = ttk.Entry(root)
labor_cost_entry.pack()

ttk.Label(root, text="Failure rate (%):").pack()
failure_rate_entry = ttk.Entry(root)
failure_rate_entry.pack()

ttk.Label(root, text="Material cost per unit ($):").pack()
material_cost_entry = ttk.Entry(root)
material_cost_entry.pack()

ttk.Label(root, text="Material used (units):").pack()
material_used_entry = ttk.Entry(root)
material_used_entry.pack()

ttk.Label(root, text="Preparation time (hours):").pack()
prep_time_entry = ttk.Entry(root)
prep_time_entry.pack()

ttk.Label(root, text="Post-processing time (hours):").pack()
post_time_entry = ttk.Entry(root)
post_time_entry.pack()

ttk.Label(root, text="Consumables cost ($):").pack()
consumables_cost_entry = ttk.Entry(root)
consumables_cost_entry.pack()

ttk.Label(root, text="Markup percentage (%):").pack()
markup_entry = ttk.Entry(root)
markup_entry.pack()

# Create a calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_cost)
calculate_button.pack(pady=10)

# Result label
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
