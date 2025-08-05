#Exception Handling in File Operations
try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("❌ File not found.")

