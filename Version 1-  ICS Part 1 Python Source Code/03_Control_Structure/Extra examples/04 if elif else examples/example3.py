#Program:Write a Python program that takes a traffic light color as input and prints the corresponding action or an error message if the color is invalid.

color = input("Enter traffic light color: ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")
'''Output
Enter traffic light color: Red  
Stop

Enter traffic light color: blue  
Invalid color
'''



