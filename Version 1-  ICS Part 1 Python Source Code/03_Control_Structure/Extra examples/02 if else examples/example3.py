#Program:Write a Python program that takes temperature in Celsius as input and prints a message based on whether it’s hot or normal.
temp = float(input("Enter temperature in °C: "))
if temp > 35:
    print("It's hot outside!")
else:
    print("Weather is normal.")

'''Output
Enter temperature in °C: 38  
It's hot outside!
'''