import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Main window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("350x550")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Header Label
title = tk.Label(
    root,
    text="Calculator Developed by Zeeshan",
    font=("Segoe UI", 14, "bold"),
    bg="#f0f0f0",
    fg="#333333",
    pady=10
)
title.pack()

# Entry display
entry = tk.Entry(root, font=("Segoe UI", 24), bd=0, relief=tk.FLAT, justify=tk.RIGHT)
entry.pack(padx=20, pady=10, fill=tk.X, ipady=15)

# Button style
button_font = ("Segoe UI", 18)
button_bg = "#ffffff"
button_active_bg = "#d4d4d4"
button_fg = "#000000"

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Button frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=10, pady=10)

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame, bg="#f0f0f0")
    row_frame.pack(fill="x", pady=5)
    for btn_text in row:
        btn = tk.Button(
            row_frame,
            text=btn_text,
            font=button_font,
            bg=button_bg,
            fg=button_fg,
            activebackground=button_active_bg,
            relief=tk.FLAT,
            width=5,
            height=2
        )
        btn.pack(side="left", expand=True, fill="both", padx=5)
        btn.bind("<Button-1>", click)

root.mainloop()
