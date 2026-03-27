from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def area(self):
        side = int(input("Enter side: "))
        print("Area:", side * side)

s = Square()
s.area()
