# Example 2: Invalid Input (int conversion)
try:
    num = int("abc")
except ValueError:
    print("That's not a valid number.")
    
# Output: That's not a valid number.
