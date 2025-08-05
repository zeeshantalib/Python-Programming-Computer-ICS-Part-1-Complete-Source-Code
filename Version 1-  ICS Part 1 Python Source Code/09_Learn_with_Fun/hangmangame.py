import tkinter as tk
import random

# Word list
words = ["python", "hangman", "school", "program", "student", "computer", "science"]

# Game variables
word = random.choice(words)
display_word = ["_"] * len(word)
guessed_letters = []
chances = 6

# Main game logic
def guess_letter():
    global chances
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter or len(letter) != 1 or not letter.isalpha():
        result_label.config(text="Enter a single alphabet.")
        return

    if letter in guessed_letters:
        result_label.config(text="You already guessed that letter.")
        return

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display_word[i] = letter
        word_label.config(text=" ".join(display_word))
        result_label.config(text="Correct guess!")
    else:
        chances -= 1
        chances_label.config(text=f"Chances Left: {chances}")
        result_label.config(text="Wrong guess!")

    guessed_label.config(text=f"Guessed: {', '.join(guessed_letters)}")

    if "_" not in display_word:
        result_label.config(text="🎉 You won! 🎉")
        guess_btn.config(state=tk.DISABLED)

    if chances == 0:
        result_label.config(text=f"You lost! Word was: {word}")
        guess_btn.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("450x350")
root.config(bg="#1e1e2f")

title = tk.Label(root, text="Hangman Game", font=("Segoe UI Black", 24), fg="#61afef", bg="#1e1e2f")
title.pack(pady=10)

word_label = tk.Label(root, text=" ".join(display_word), font=("Segoe UI", 22), fg="white", bg="#1e1e2f")
word_label.pack(pady=10)

chances_label = tk.Label(root, text=f"Chances Left: {chances}", font=("Segoe UI", 14), fg="#e06c75", bg="#1e1e2f")
chances_label.pack()

guessed_label = tk.Label(root, text="Guessed: ", font=("Segoe UI", 12), fg="#98c379", bg="#1e1e2f")
guessed_label.pack(pady=5)

entry = tk.Entry(root, font=("Segoe UI", 14), width=5, justify='center')
entry.pack(pady=5)
entry.focus()

guess_btn = tk.Button(root, text="Guess", font=("Segoe UI", 14), bg="#61afef", fg="white", command=guess_letter)
guess_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Segoe UI", 12), fg="white", bg="#1e1e2f")
result_label.pack()

root.mainloop()
