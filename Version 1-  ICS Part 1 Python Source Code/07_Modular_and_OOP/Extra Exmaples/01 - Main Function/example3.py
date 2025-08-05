# Title: Call multiple functions from main

def greet():
    print("Hello!")

def bye():
    print("Goodbye!")

def main():
    greet()
    bye()

if __name__ == "__main__":
    main()

# Output:
# Hello!
# Goodbye!
