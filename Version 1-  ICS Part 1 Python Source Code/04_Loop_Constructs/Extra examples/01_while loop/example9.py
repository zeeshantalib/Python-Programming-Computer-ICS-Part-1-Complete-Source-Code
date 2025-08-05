#Age Validation

age = int(input("Enter your age: "))
while age < 18:
    print("You must be 18+.")
    age = int(input("Re-enter age: "))
print("Access granted.")


'''Output
Enter your age: 15
You must be 18+.
Re-enter age: 18
Access granted.
'''



