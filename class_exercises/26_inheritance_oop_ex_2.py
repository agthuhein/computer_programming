class Shape:
    def area(self):
        return 0
    

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def area(self):
        return self.l * self.w


class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h

r1 = Rectangle(5, 7)
print(f"The area of rectangle is {r1.area()}")

t1 = Triangle(5, 6)
print(f"The area of triangle is {t1.area()}")