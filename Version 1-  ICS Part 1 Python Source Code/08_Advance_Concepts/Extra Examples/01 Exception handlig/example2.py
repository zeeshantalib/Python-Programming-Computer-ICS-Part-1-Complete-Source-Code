# Example 4: Index Error in List
try:
    nums = [1, 2, 3]
    print(nums[5])
except IndexError:
    print("Index is out of range.")
# Output: Index is out of range.
