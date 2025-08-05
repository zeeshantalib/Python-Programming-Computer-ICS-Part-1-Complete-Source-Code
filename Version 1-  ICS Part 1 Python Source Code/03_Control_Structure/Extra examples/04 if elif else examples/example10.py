#Program:Write a Python program that takes age as input and prints the ticket price based on age groups.
age = int(input("Enter your age: "))
if age <= 12:
    print("Ticket: Rs. 100")
elif age <= 60:
    print("Ticket: Rs. 200")
else:
    print("Ticket: Rs. 150")

'''Output
Enter your age: 10  
Ticket: Rs. 100

Enter your age: 70  
Ticket: Rs. 150
'''