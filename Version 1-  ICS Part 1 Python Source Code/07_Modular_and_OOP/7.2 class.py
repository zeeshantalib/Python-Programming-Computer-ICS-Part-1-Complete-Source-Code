class ToyCar:
# The _ _init_ _ method in idealizes the object with specific attributes
    def __init__(self , color, size , wheels):
        self.color = color # Color of the toy car
        self.size = size # Size of the toy car
        self.wheels = wheels # Number of wheels in toy car
    # Method to describe the
    def describe(self):
        return "This toy car is" , self.color , "size", self.size, "and has " ,
        self.wheels , "Wheels."

# Create objects of the ToyCar class
car1 = ToyCar("red", "small", 4)
car2 = ToyCar("blue", "large", 6)

# Print descriptions of the
print(car1.describe( ))
print(car2.describe( ))
