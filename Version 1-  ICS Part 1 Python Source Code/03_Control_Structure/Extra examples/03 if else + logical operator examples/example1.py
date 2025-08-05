#Program:Write a Python program that takes a score as input and prints whether the score is valid (between 0 and 100) or invalid.
score = int(input("Enter score: "))
if not (0 <= score <= 100):
    print("Invalid score")
else:
    print("Valid score")

'''
Output
Enter score: 85  
Valid score
'''


