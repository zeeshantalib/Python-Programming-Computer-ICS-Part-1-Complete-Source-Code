#Program:Write a Python program that takes two numbers and an operator as input, performs the corresponding arithmetic operation, and prints the result.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")
    
'''Output
Enter first number: 10  
Enter second number: 5  
Enter operator (+, -, *, /): +  
Result: 15.0

Enter first number: 10  
Enter second number: 5  
Enter operator (+, -, *, /): %  
Invalid operator
'''


