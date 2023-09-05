import Student

a = Student.Student("이동준",34)

from Student import *
b = Student("박유상",30)

a.introduce()
b.introduce()