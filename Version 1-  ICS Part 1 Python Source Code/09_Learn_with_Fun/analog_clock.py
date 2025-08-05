import tkinter as tk
import time
import math

# Setup main window
root = tk.Tk()
root.title("Analog Clock by Zeeshan")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

canvas = tk.Canvas(root, width=400, height=400, bg="white", highlightthickness=0)
canvas.pack(pady=10)

# Clock center
center_x, center_y = 200, 200
radius = 180

def draw_clock_face():
    # Outer circle
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill="#ffffff", outline="#000000", width=4)

    # Numbers and tick marks
    for i in range(60):
        angle = math.radians(i * 6)
        x_outer = center_x + radius * math.sin(angle)
        y_outer = center_y - radius * math.cos(angle)

        if i % 5 == 0:
            # Hour marks
            x_inner = center_x + (radius - 20) * math.sin(angle)
            y_inner = center_y - (radius - 20) * math.cos(angle)
            canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=3)
            
            num = i // 5 or 12
            x_text = center_x + (radius - 40) * math.sin(angle)
            y_text = center_y - (radius - 40) * math.cos(angle)
            canvas.create_text(x_text, y_text, text=str(num), font=("Segoe UI", 12, "bold"))
        else:
            # Minute marks
            x_inner = center_x + (radius - 10) * math.sin(angle)
            y_inner = center_y - (radius - 10) * math.cos(angle)
            canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=1)

def update_clock():
    canvas.delete("hands")
    t = time.localtime()
    sec = t.tm_sec
    min = t.tm_min
    hr = t.tm_hour % 12

    # Angles
    sec_angle = math.radians(sec * 6)
    min_angle = math.radians(min * 6 + sec * 0.1)
    hr_angle = math.radians(hr * 30 + min * 0.5)

    # Hands
    sec_len = 140
    min_len = 110
    hr_len = 80

    # Second hand
    x_sec = center_x + sec_len * math.sin(sec_angle)
    y_sec = center_y - sec_len * math.cos(sec_angle)
    canvas.create_line(center_x, center_y, x_sec, y_sec, fill="red", width=1.5, tags="hands")

    # Minute hand
    x_min = center_x + min_len * math.sin(min_angle)
    y_min = center_y - min_len * math.cos(min_angle)
    canvas.create_line(center_x, center_y, x_min, y_min, fill="black", width=3, tags="hands")

    # Hour hand
    x_hr = center_x + hr_len * math.sin(hr_angle)
    y_hr = center_y - hr_len * math.cos(hr_angle)
    canvas.create_line(center_x, center_y, x_hr, y_hr, fill="black", width=5, tags="hands")

    # Center circle
    canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="black", tags="hands")

    root.after(1000, update_clock)

# Draw static parts
draw_clock_face()
update_clock()

# Footer label
footer = tk.Label(root, text="Analog Clock by Zeeshan", font=("Segoe UI", 12), bg="#f0f0f0")
footer.pack(pady=5)

root.mainloop()
