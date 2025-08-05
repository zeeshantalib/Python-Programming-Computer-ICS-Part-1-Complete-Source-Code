import tkinter as tk
import time

# Create main window
root = tk.Tk()
root.title("Digital Clock by Zeeshan")
root.geometry("400x200")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Clock label
clock_label = tk.Label(
    root,
    font=("Segoe UI", 48, "bold"),
    fg="#39FF14",
    bg="#1e1e1e"
)
clock_label.pack(expand=True)

# Footer
footer = tk.Label(
    root,
    text="Digital Clock by Zeeshan",
    font=("Segoe UI", 12),
    fg="#CCCCCC",
    bg="#1e1e1e"
)
footer.pack(pady=5)

# Update function
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_time)

update_time()
root.mainloop()
