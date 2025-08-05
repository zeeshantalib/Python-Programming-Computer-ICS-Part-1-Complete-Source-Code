import tkinter as tk
from tkinter import messagebox

# Function definitions
def show_entry():
    name = entry.get()
    messagebox.showinfo("Entry Data", f"Hello, {name}")

def draw_shapes():
    canvas.delete("all")
    canvas.create_line(10, 10, 200, 10, fill="blue", width=3)
    canvas.create_rectangle(10, 20, 100, 80, fill="lightgreen")
    canvas.create_oval(120, 20, 200, 80, fill="red")
    canvas.create_text(100, 100, text="Canvas Shapes", font=("Arial", 12))

def update_label():
    selected = radio_var.get()
    label.config(text=f"Selected Option: {selected}")

def show_warning():
    messagebox.showwarning("Warning", "This is just a warning!")

def move_canvas_item():
    canvas.move(ball, 10, 0)

# Main window
root = tk.Tk()
root.title("Tkinter Demo - All Functions")
root.geometry("600x500")
root.resizable(False, False)

# Label
label = tk.Label(root, text="Welcome to Tkinter Demo", font=("Arial", 14))
label.pack(pady=10)

# Entry widget + Button
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit Name", command=show_entry).pack(pady=5)

# Canvas and drawing
canvas = tk.Canvas(root, width=300, height=150, bg="white")
canvas.pack(pady=10)

tk.Button(root, text="Draw Shapes", command=draw_shapes).pack()

# Move shape example
ball = canvas.create_oval(10, 120, 40, 150, fill="purple")
tk.Button(root, text="Move Ball →", command=move_canvas_item).pack(pady=5)

# Radiobuttons
radio_var = tk.StringVar(value="Option 1")
radio_frame = tk.Frame(root)
radio_frame.pack(pady=5)

tk.Radiobutton(radio_frame, text="Option 1", variable=radio_var, value="Option 1", command=update_label).pack(side=tk.LEFT)
tk.Radiobutton(radio_frame, text="Option 2", variable=radio_var, value="Option 2", command=update_label).pack(side=tk.LEFT)

# Checkbox
chk_var = tk.BooleanVar()
tk.Checkbutton(root, text="Accept Terms", variable=chk_var).pack()

# Scale
tk.Label(root, text="Volume").pack()
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

# Spinbox
tk.Label(root, text="Choose Number").pack()
spin = tk.Spinbox(root, from_=1, to=10)
spin.pack()

# Listbox
tk.Label(root, text="Languages").pack()
listbox = tk.Listbox(root)
for lang in ["Python", "Java", "C++", "JavaScript"]:
    listbox.insert(tk.END, lang)
listbox.pack()

# Warning button
tk.Button(root, text="Show Warning", command=show_warning).pack(pady=5)

# Quit button
tk.Button(root, text="Quit", command=root.destroy).pack(pady=5)

# Handle close button
def on_closing():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the GUI
root.mainloop()
