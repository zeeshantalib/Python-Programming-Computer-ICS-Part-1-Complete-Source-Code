#Program:Write a Python program that takes battery percentage and device temperature as input and prints a warning if battery is below 10% or temperature is above 45°C; otherwise, prints that the device is safe.
battery = int(input("Battery %: "))
temperature = int(input("Device temperature °C: "))
if battery < 10 or temperature > 45:
    print("Warning: Device critical!")
else:
    print("Device is safe")

'''Output
Battery %: 8  
Device temperature °C: 40  
Warning: Device critical!'''




