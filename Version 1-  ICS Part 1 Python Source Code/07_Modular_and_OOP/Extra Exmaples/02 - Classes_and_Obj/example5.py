# Title: Student Information using Constructor

class Student:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def show_info(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student(1, "Ali", 1000)
s1.show_info()

# Output:
# Roll No: 1, Name: Ali, Marks: 1000
