class Student:
    def __init__(self, name, age): #메모리 생성시 자동 호출
        self.name = name
        self.age = age
    def __del__(self): #메모리가 소멸될 때 자동 호출
        print("메모리삭제")
    def introduce(self):
        print(f"이름:{self.name}, 나이:{self.age}")
a = Student("이동준",34) #암묵적으로 순서에 맞게끔 값을 대입함
b = Student(age=30, name="박유상") #매개변수를 명시화
a.introduce()
b.introduce()
print(a) #<__main__.Student object at 0x00000211C2DB1110>