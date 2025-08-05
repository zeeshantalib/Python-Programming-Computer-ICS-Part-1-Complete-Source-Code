#Keep asking until correct password

password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted")


'''Output
Enter password: abc
Enter password: 999
Enter password: 1234
Access granted
'''



