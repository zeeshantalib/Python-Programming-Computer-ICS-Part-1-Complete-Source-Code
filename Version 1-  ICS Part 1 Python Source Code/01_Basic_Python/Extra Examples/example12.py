#Program:Write a Python program that takes time in hours as input, converts it to minutes and seconds, and prints both results.
hours = float(input("Enter time in hours: "))
minutes = hours * 60
seconds = hours * 3600
print("Minutes:", minutes)
print("Seconds:", seconds)

'''Output
Enter time in hours: 2.5  
Minutes: 150.0  
Seconds: 9000.0
'''