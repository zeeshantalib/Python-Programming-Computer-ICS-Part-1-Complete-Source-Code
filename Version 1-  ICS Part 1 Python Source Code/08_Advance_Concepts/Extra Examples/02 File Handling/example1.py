
# Write text to a file (overwrites if file exists)
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("Python file handling is easy!\n")

# ✅ Output in example.txt:
# Hello, this is the first line.
# Python file handling is easy!
