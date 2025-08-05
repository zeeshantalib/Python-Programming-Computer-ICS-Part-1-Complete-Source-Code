# Append new lines to the file
with open("example.txt", "a") as file:
    file.write("Adding a third line.\n")

# ✅ example.txt now contains:
# Hello, this is the first line.
# Python file handling is easy!
# Adding a third line.
