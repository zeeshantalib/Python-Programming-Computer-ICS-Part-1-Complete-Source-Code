#Program:Write a Python program that takes age and degree status as input and prints whether the person is eligible for the job or not.
age = int(input("Enter age: "))
has_degree = input("Do you have a degree? (yes/no): ").lower()
if age >= 21 and has_degree == "yes":
    print("Eligible for the job")
else:
    print("Not eligible")

'''Output
Enter age: 25  
Do you have a degree? (yes/no): yes  
Eligible for the job
'''