#Program:Write a Python program that takes a username as input and prints a welcome message if the username is "admin" (case-insensitive), otherwise prints access denied.
username = input("Enter username: ")
if username.lower() == "admin":
    print("Welcome, admin!")
else:
    print("Access denied")


'''Output
Enter username: Admin  
Welcome, admin!'''



