# Example 3: File Not Found
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found.")
# Output: File not found.
