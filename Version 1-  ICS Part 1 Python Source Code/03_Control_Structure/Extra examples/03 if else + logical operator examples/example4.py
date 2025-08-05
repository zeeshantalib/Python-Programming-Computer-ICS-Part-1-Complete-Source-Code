#Program:Write a Python program that takes body temperature in °F as input and prints whether it is normal or abnormal.
temp = int(input("Enter body temperature in °F: "))
if not (97 <= temp <= 99):
    print("Abnormal temperature")
else:
    print("Normal temperature")
'''
Output
Enter body temperature in °F: 98  
Normal temperature
'''




