width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def area(self):
        return 0.5 * self.width * self.height

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

triangle = Triangle(width, height)
print("Triangle area:", triangle.area())

rectangle = Rectangle(width, height)
print("Rectangle area:", rectangle.area())