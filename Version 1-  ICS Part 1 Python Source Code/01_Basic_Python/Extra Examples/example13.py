#Program:Write a Python program that takes a number of days as input and prints the equivalent in years, weeks, and days.
days = int(input("Enter number of days: "))
years = days // 365
weeks = (days % 365) // 7
remaining_days = days % 7
print("Years:", years, "Weeks:", weeks, "Days:", remaining_days)

'''Output
Enter number of days: 800  
Years: 2 Weeks: 9 Days: 2
'''