import tkinter as tk
from tkinter import messagebox
import math

def calculate_area():
    try:
        radius = float(entry_radius.get())
        if radius < 0:
            raise ValueError("Negative radius")
        area = math.pi * radius ** 2
        label_result.config(text=f"Area: {area:.2f} square units")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid positive number for radius.")

# Create main window
root = tk.Tk()
root.title("Circle Area Calculator")
root.geometry("300x180")
root.resizable(False, False)

# Radius input
tk.Label(root, text="Enter radius:", font=("Arial", 12)).pack(pady=10)
entry_radius = tk.Entry(root, font=("Arial", 12), justify="center")
entry_radius.pack()

# Calculate button
btn_calc = tk.Button(root, text="Calculate Area", font=("Arial", 12), command=calculate_area)
btn_calc.pack(pady=15)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
label_result.pack()

root.mainloop()
