# Example 7: Multiple Exceptions
try:
    a = int("abc")
    b = 10 / 0
except ValueError:
    print("Value Error occurred.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
# Output: Value Error occurred.
