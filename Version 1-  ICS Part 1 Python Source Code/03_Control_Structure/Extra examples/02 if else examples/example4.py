#Program:Write a Python program that takes file size in MB as input and prints whether it is acceptable or too large to upload.
size = float(input("Enter file size in MB: "))
if size < 25:
    print("File size is acceptable.")
else:
    print("File too large to upload.")

'''Output
Enter file size in MB: 20  
File size is acceptable.
'''