#Program:Write a Python program that takes a choice number as input and prints the selected drink or an error message for invalid choices.
choice = int(input("Enter 1 for Tea, 2 for Coffee, 3 for Juice: "))
if choice == 1:
    print("You selected Tea")
elif choice == 2:
    print("You selected Coffee")
elif choice == 3:
    print("You selected Juice")
else:
    print("Invalid choice")
'''Output
Enter 1 for Tea, 2 for Coffee, 3 for Juice: 2  
You selected Coffee

Enter 1 for Tea, 2 for Coffee, 3 for Juice: 4  
Invalid choice'''



