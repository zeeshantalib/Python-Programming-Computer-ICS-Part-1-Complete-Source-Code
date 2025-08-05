import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Initialize scores
user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = f"Both chose {user_choice}. It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        user_score += 1
        result = f"You chose {user_choice}. Computer chose {comp_choice}. You Win!"
    else:
        comp_score += 1
        result = f"You chose {user_choice}. Computer chose {comp_choice}. You Lose!"

    result_label.config(text=result)
    score_label.config(text=f"Your Score: {user_score}   Computer Score: {comp_score}")

# Setup window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x300")
root.config(bg="#282c34")

title = tk.Label(root, text="Rock, Paper, Scissors", font=("Segoe UI Black", 20), fg="#61afef", bg="#282c34")
title.pack(pady=15)

frame = tk.Frame(root, bg="#282c34")
frame.pack(pady=10)

btn_rock = tk.Button(frame, text="🪨 Rock", font=("Segoe UI", 14), width=10, bg="#98c379", fg="black", command=lambda: play("Rock"))
btn_paper = tk.Button(frame, text="📄 Paper", font=("Segoe UI", 14), width=10, bg="#e5c07b", fg="black", command=lambda: play("Paper"))
btn_scissors = tk.Button(frame, text="✂️ Scissors", font=("Segoe UI", 14), width=10, bg="#e06c75", fg="black", command=lambda: play("Scissors"))

btn_rock.grid(row=0, column=0, padx=10)
btn_paper.grid(row=0, column=1, padx=10)
btn_scissors.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Segoe UI", 14), fg="white", bg="#282c34", wraplength=380)
result_label.pack(pady=20)

score_label = tk.Label(root, text="Your Score: 0   Computer Score: 0", font=("Segoe UI", 14, "bold"), fg="#56b6c2", bg="#282c34")
score_label.pack()

root.mainloop()
