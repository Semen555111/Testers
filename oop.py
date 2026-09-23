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

class Book:
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
print(Book.__doc__)



