#Number guessing game

secret = 7
guess = -1
while guess != secret:
    guess = int(input("Guess the number (1–10): "))
print("Correct!")

'''Output
Guess the number (1–10): 3
Guess the number (1–10): 9
Guess the number (1–10): 7
Correct!'''
