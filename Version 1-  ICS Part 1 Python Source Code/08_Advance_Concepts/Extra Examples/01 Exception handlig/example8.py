try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
except ValueError:
    print("❌ Invalid input. Please enter a number.")
else:
    print("✅ Result:", result)
finally:
    print("✨ Program finished.")
    
# Output:
# Enter a number: 0
# ❌ Cannot divide by zero.
# ✨ Program finished.