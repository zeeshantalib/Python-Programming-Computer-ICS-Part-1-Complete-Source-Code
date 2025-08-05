# Title: main() using return value from a function

def add(a, b):
    return a + b

def main():
    result = add(5, 3)
    print("Sum is:", result)

if __name__ == "__main__":
    main()

# Output:
# Sum is: 8
