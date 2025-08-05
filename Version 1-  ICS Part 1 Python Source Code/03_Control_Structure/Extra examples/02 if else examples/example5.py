#Program:Write a Python program that takes speed in km/h as input and prints whether it is within the limit or over-speeding.
speed = int(input("Enter your speed in km/h: "))
if speed <= 120:
    print("Speed is within limit.")
else:
    print("Over-speeding! Slow down.")

'''Output
Enter your speed in km/h: 100  
Speed is within limit.
'''