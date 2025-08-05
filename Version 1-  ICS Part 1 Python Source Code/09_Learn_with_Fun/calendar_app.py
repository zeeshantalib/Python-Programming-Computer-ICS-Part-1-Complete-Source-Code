import tkinter as tk
import calendar

def show_calendar():
    year = int(year_entry.get())
    cal_text = calendar.TextCalendar(firstweekday=0).formatyear(year)
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, cal_text)

# Create main window
root = tk.Tk()
root.title("Calendar by Zeeshan")
root.geometry("500x600")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Calendar by Zeeshan", font=("Segoe UI", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Year input
year_frame = tk.Frame(root, bg="#f0f0f0")
year_frame.pack(pady=10)

year_label = tk.Label(year_frame, text="Enter Year:", font=("Segoe UI", 12), bg="#f0f0f0")
year_label.pack(side=tk.LEFT, padx=5)

year_entry = tk.Entry(year_frame, font=("Segoe UI", 12), width=10)
year_entry.pack(side=tk.LEFT, padx=5)

show_btn = tk.Button(year_frame, text="Show Calendar", font=("Segoe UI", 12), command=show_calendar)
show_btn.pack(side=tk.LEFT, padx=5)

# Text area for calendar display
text_area = tk.Text(root, font=("Courier New", 10), width=60, height=30, borderwidth=2, relief="groove")
text_area.pack(pady=10)

root.mainloop()
