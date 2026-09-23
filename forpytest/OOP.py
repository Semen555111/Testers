"""class Point:
    color = 'red'
    circle = 2
a = Point
b = Point
Point.circle = 1
print(a.circle, b.circle)# Выводим объект citcle который хранится в Point, но через внешние a и b
print(a.__dict__)
print(b.__dict__)
print(Point.__dict__)# В 3 предыдущих принтах и в этом выводится color = 'green', так как поменяв его в объекте, он поменялся и в классе
a.color = 'green'
delattr(a, 'color')"""

#------------------------

'''class Book:
    "Pages of website"
    author = 'Samuel'
    title = 'Govno'
    pages = 153
a,b = Book,Book
a.Price = 167
b.Price = 194
print(Book.__dict__)
print(a.__dict__)
print(b.__dict__)
print(Book.__doc__)'''
#-----------------------------------
'''class User:
    X = 1
data = {'name': 'Иван', 'age': 20, 'city': 'Москва'}
u = User
for key, value in data.items():
    setattr(u,key,value)
if (hasattr(u, 'city')):
    delattr(u,'city')
print(u.__dict__)'''
#----------------------------


class Calc():
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a*b
    def divide(self,a,b):
        return a/b
u = Calc()
print(u.add(3, 4))

class CAR:
    ""
    def drive(self, km):
        if km > 0:
            self.milege += km
    def get_info(self):
        return self.brand + " " + self.model
car = CAR()
car.brand = 'BMW'
car.model = 'M5'
car.milege = 10000
class Student:
    def add_grade(self, grade):
        if 1<=grade<=5:
            self.grades.append(grade)
        else:
            return 'Нормальное число введи дятел'
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
student = Student()
student.name = "Alex"
student.grades = [] 
class User:
    ins = None
    def __new__(cls, name):
        if cls.ins is None:
            cls.ins = super().__new__(cls)
        return cls.ins
    def __init__(self,name):
        self.name = name

user1 = User('Alex')
user2 = User('Bob')
print(user1.name, user2.name)