#Program:Write a Python program that takes the number of login attempts as input and prints whether the account is locked or the user can try again.
attempts = int(input("Enter number of login attempts: "))
if attempts >= 3:
    print("Account locked")
else:
    print("You can try again")

'''Output
Enter number of login attempts: 2  
You can try again
'''