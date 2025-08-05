#Program:Write a Python program that takes a user role as input and prints "Access granted" if the role is "admin" or "superuser" (case-insensitive), otherwise prints "Access denied".
role = input("Enter your role: ").lower()
if role == "admin" or role == "superuser":
    print("Access granted")
else:
    print("Access denied")

'''Output
Enter your role: Admin  
Access granted
'''


