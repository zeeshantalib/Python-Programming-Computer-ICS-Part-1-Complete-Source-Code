#Getter Setter
class Student:
    def set_info(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks
    def get_info(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)

# Creating and displaying the student object
s1=Student()
s1.set_info(1,"Zeeshan",90)
s1.get_info()


