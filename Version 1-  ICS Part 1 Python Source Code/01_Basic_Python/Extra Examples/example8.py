#Program:Write a Python program that takes distance and time as input, calculates the speed, and prints the result
distance = float(input("Enter distance (km): "))
time = float(input("Enter time (hr): "))
speed = distance / time
print("Speed:", speed, "km/hr")
'''Output
Enter distance (km): 120  
Enter time (hr): 2  
Speed: 60.0 km/hr
'''