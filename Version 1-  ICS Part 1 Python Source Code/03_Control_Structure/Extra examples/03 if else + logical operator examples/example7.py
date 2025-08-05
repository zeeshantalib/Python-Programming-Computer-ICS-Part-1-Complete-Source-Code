#Program:Write a Python program that takes a username and password as input and prints "Login successful" if both match predefined values, otherwise prints "Login failed".
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")

'''Output
Enter username: admin  
Enter password: 1234  
Login successful'''
