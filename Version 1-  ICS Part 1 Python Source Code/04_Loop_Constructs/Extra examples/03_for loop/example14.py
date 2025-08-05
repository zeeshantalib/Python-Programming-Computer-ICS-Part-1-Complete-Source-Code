#Sum of even numbers (1–10)

total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i
print("Sum of even numbers:", total)

'''Output
Sum of even numbers: 30
'''