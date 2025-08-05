#Program:Write a Python program that takes weight and height as input, calculates the BMI, and prints the result.
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)
print("BMI:", bmi)
'''Enter weight (kg): 70  
Enter height (m): 1.75  
BMI: 22.857142857142858
'''