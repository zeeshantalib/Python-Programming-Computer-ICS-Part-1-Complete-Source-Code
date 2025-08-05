#Program:Write a Python program that takes annual income as input and prints the applicable tax rate based on income slabs.
income = int(input("Enter your annual income: "))
if income <= 250000:
    print("No tax")
elif income <= 500000:
    print("5% tax")
elif income <= 1000000:
    print("20% tax")
else:
    print("30% tax")

'''Output
Enter your annual income: 400000  
5% tax

Enter your annual income: 1500000  
30% tax'''
