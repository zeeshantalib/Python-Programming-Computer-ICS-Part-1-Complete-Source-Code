#Program:Write a Python program that takes a day number (1-7) as input and prints the corresponding day name, or an error message if the number is invalid
day = int(input("Enter day number (1-7): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")

'''Output
Enter day number (1-7): 3  
Wednesday
 
Enter day number (1-7): 7  
Sunday

Enter day number (1-7): 9  
Invalid day number

etc…
'''
