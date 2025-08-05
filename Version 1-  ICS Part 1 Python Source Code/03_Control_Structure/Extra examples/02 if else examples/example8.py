#Program:Write a Python program that takes battery percentage as input and prints a warning if it's low, otherwise confirms the battery is okay.
battery = int(input("Enter battery percentage: "))
if battery < 20:
    print("Low battery, please charge!")
else:
    print("Battery level is okay")


'''Output
Enter battery percentage: 15  
Low battery, please charge!'''



