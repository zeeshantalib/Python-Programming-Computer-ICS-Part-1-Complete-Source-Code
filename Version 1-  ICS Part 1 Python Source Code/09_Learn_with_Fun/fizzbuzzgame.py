import tkinter as tk
from tkinter import scrolledtext

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

def run_fizzbuzz():
    output_box.delete(1.0, tk.END)
    try:
        n = int(entry.get())
        if n <= 0:
            output_box.insert(tk.END, "Please enter a positive integer.")
            return
        results = fizzbuzz(n)
        output_box.insert(tk.END, "\n".join(results))
    except ValueError:
        output_box.insert(tk.END, "Invalid input! Please enter a valid integer.")

root = tk.Tk()
root.title("FizzBuzz GUI")
root.geometry("400x450")
root.config(bg="#282c34")

label = tk.Label(root, text="Enter a number:", font=("Segoe UI", 14), fg="white", bg="#282c34")
label.pack(pady=10)

entry = tk.Entry(root, font=("Segoe UI", 14), justify='center')
entry.pack(pady=5)
entry.focus()

run_button = tk.Button(root, text="Run FizzBuzz", font=("Segoe UI", 14, "bold"), bg="#61afef", fg="white", command=run_fizzbuzz)
run_button.pack(pady=10)

output_box = scrolledtext.ScrolledText(root, width=40, height=15, font=("Consolas", 12))
output_box.pack(pady=10)
output_box.config(state=tk.NORMAL, bg="#1e2127", fg="#abb2bf", insertbackground='white')

root.mainloop()
