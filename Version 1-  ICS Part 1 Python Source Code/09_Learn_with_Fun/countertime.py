import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("400x280")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E2F")

        self.time_left = 0
        self.timer_running = False
        self.paused = False

        # Title label
        title = tk.Label(root, text="Countdown Timer", font=("Segoe UI", 20, "bold"),
                         bg="#1E1E2F", fg="#ECF0F1")
        title.pack(pady=(15, 5))

        # Input frame
        input_frame = tk.Frame(root, bg="#1E1E2F")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter time (seconds):", font=("Segoe UI", 14),
                 bg="#1E1E2F", fg="#BDC3C7").grid(row=0, column=0, padx=5, sticky="e")

        self.entry = tk.Entry(input_frame, font=("Segoe UI", 16), width=8, justify="center",
                              bd=2, relief="groove")
        self.entry.grid(row=0, column=1, padx=5)

        # Buttons frame
        btn_frame = tk.Frame(root, bg="#1E1E2F")
        btn_frame.pack(pady=15)

        btn_style = {
            "font": ("Segoe UI", 12, "bold"),
            "width": 8,
            "bd": 0,
            "relief": "ridge",
            "cursor": "hand2",
            "fg": "white",
            "pady": 6,
        }

        self.start_btn = tk.Button(btn_frame, text="Start", bg="#27AE60", activebackground="#2ECC71", **btn_style,
                                   command=self.start_countdown)
        self.start_btn.grid(row=0, column=0, padx=8)

        self.pause_btn = tk.Button(btn_frame, text="Pause", bg="#F39C12", activebackground="#F1C40F", state="disabled", **btn_style,
                                   command=self.pause_timer)
        self.pause_btn.grid(row=0, column=1, padx=8)

        self.resume_btn = tk.Button(btn_frame, text="Resume", bg="#2980B9", activebackground="#3498DB", state="disabled", **btn_style,
                                    command=self.resume_timer)
        self.resume_btn.grid(row=0, column=2, padx=8)

        self.reset_btn = tk.Button(btn_frame, text="Reset", bg="#C0392B", activebackground="#E74C3C", state="disabled", **btn_style,
                                   command=self.reset_timer)
        self.reset_btn.grid(row=0, column=3, padx=8)

        # Timer display frame for better centering
        display_frame = tk.Frame(root, bg="#1E1E2F")
        display_frame.pack(pady=(10, 20), fill="x")

        self.label = tk.Label(display_frame, text="", font=("Segoe UI", 52, "bold"),
                              fg="#E74C3C", bg="#1E1E2F")
        self.label.pack(expand=True)

    def start_countdown(self):
        if self.timer_running:
            return

        try:
            self.time_left = int(self.entry.get())
            if self.time_left <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a positive integer.")
            return

        self.timer_running = True
        self.paused = False

        self.start_btn.config(state="disabled")
        self.pause_btn.config(state="normal")
        self.resume_btn.config(state="disabled")
        self.reset_btn.config(state="normal")
        self.entry.config(state="disabled")

        self.update_timer()

    def update_timer(self):
        if not self.timer_running or self.paused:
            return

        mins, secs = divmod(self.time_left, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        self.label.config(text=time_format)

        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_running = False
            self.start_btn.config(state="normal")
            self.pause_btn.config(state="disabled")
            self.resume_btn.config(state="disabled")
            self.reset_btn.config(state="disabled")
            self.entry.config(state="normal")
            messagebox.showinfo("Time's up!", "Countdown finished!")

    def pause_timer(self):
        if self.timer_running and not self.paused:
            self.paused = True
            self.pause_btn.config(state="disabled")
            self.resume_btn.config(state="normal")

    def resume_timer(self):
        if self.timer_running and self.paused:
            self.paused = False
            self.pause_btn.config(state="normal")
            self.resume_btn.config(state="disabled")
            self.update_timer()

    def reset_timer(self):
        self.timer_running = False
        self.paused = False
        self.time_left = 0
        self.label.config(text="")
        self.start_btn.config(state="normal")
        self.pause_btn.config(state="disabled")
        self.resume_btn.config(state="disabled")
        self.reset_btn.config(state="disabled")
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
