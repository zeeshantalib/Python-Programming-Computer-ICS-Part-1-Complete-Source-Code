# Example 8: Finally Block
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error occurred.")
finally:
    print("This always runs.")
# Output:
# Error occurred.
# This always runs.
