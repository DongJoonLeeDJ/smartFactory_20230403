class Student:
    def __init__(self, name, age): #메모리 생성시 자동 호출
        self.name = name
        self.age = age
    def __del__(self): #메모리가 소멸될 때 자동 호출
        print("메모리삭제")
    def introduce(self):
        print(f"이름:{self.name}, 나이:{self.age}")