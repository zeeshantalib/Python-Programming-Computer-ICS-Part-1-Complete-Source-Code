#Read File Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# ✅ Output (one line at a time, no extra newline):
# Hello, this is the first line.
# Python file handling is easy!
# Adding a third line.
