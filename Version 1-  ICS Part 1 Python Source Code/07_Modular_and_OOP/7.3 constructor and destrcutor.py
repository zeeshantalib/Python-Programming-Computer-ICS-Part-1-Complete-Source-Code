class Car:
    def __init__(self, color):
        self . color = color
    def __del__(self) :
        print("Car with color", self.color , "is being deleted.")