class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    
    def cal_area(self):
        return self.width * self.height
    

    def cal_perimeter(self):
        return 2 * (self.width + self.height)


r1 = Rectangle(5.555, 5)
print(f"The area of the rectangle is {r1.cal_area()}")
print(f"The perimeter of the rectangle is {r1.cal_perimeter()}")