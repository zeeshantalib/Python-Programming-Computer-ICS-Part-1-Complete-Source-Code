#Program:Write a Python program that takes age as input and prints the age group
age = int(input("Enter age: "))
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

'''Output
Enter age: 10  
Child

Enter age: 65  
Senior'''



