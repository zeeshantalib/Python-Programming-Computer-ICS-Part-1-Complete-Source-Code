#Program:Write a Python program that takes temperature in Celsius as input and prints whether it is Freezing, Cold, Warm, or Hot.
temp = float(input("Enter temperature in °C: "))
if temp < 0:
    print("Freezing")
elif temp < 10:
    print("Cold")
elif temp < 25:
    print("Warm")
else:
    print("Hot")

'''Output
Enter temperature in °C: -5  
Freezing

Enter temperature in °C: 30  
Hot
'''


