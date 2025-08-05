import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Length Error", "Minimum length is 4.")
            return
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid number.")
        return

    # Gather selected character sets
    char_pool = ""
    if var_upper.get():
        char_pool += string.ascii_uppercase
    if var_lower.get():
        char_pool += string.ascii_lowercase
    if var_numbers.get():
        char_pool += string.digits
    if var_symbols.get():
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showerror("Selection Error", "Select at least one character type.")
        return

    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    result_label.config(text="✔️ Password generated!")

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        result_label.config(text="📋 Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("450x400")
root.config(bg="#1e1e2f")

tk.Label(root, text="🔐 Password Generator", font=("Segoe UI Black", 22), fg="#61afef", bg="#1e1e2f").pack(pady=15)

frame_options = tk.Frame(root, bg="#1e1e2f")
frame_options.pack()

tk.Label(frame_options, text="Password Length:", font=("Segoe UI", 12), fg="#abb2bf", bg="#1e1e2f").grid(row=0, column=0, sticky="w", padx=5, pady=5)
length_entry = tk.Entry(frame_options, font=("Segoe UI", 12), width=10, justify='center')
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1, pady=5)

# Checkboxes for character types
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper, font=("Segoe UI", 11),
               bg="#1e1e2f", fg="#c678dd", activebackground="#1e1e2f").pack(anchor='w', padx=30)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower, font=("Segoe UI", 11),
               bg="#1e1e2f", fg="#98c379", activebackground="#1e1e2f").pack(anchor='w', padx=30)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, font=("Segoe UI", 11),
               bg="#1e1e2f", fg="#e5c07b", activebackground="#1e1e2f").pack(anchor='w', padx=30)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, font=("Segoe UI", 11),
               bg="#1e1e2f", fg="#e06c75", activebackground="#1e1e2f").pack(anchor='w', padx=30)

tk.Button(root, text="Generate Password", font=("Segoe UI", 12), bg="#61afef", fg="white",
          command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, font=("Segoe UI", 14), width=30, justify='center')
password_entry.pack(pady=10)

tk.Button(root, text="Copy to Clipboard", font=("Segoe UI", 12), bg="#98c379", fg="black",
          command=copy_password).pack(pady=5)

result_label = tk.Label(root, text="", font=("Segoe UI", 11), fg="#56b6c2", bg="#1e1e2f")
result_label.pack(pady=5)

root.mainloop()
