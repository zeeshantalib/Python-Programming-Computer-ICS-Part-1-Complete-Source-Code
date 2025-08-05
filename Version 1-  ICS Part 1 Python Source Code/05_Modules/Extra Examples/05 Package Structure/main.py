#from file within same folder
import student
student.study()

import student as s
s.study()

# from another folder  Animal
from Animal import cat
cat.meown()
cat.run()

#from another folder Animal
from Animal import dog
dog.bark()
dog.run()

# from another Folder in Sub folder Animal/Jungle
from Animal.Jungle import lion
lion.roar()
lion.run()

