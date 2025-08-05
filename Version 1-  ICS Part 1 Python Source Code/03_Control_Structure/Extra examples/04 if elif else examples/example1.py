#Program:Write a Python program that takes marks as input and prints the grade based on the marks.
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 33:
    print("Grade D")
else:
    print("Fail")

'''Output
Enter your marks: 95  
Grade A

Enter your marks: 65  
Grade C

Enter your marks: 40  
Grade D

etc…
'''
