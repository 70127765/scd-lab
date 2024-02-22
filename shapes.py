import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width
    
    def perimeter(self):
        return 2 * (self._length + self._width)

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self._radius

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(5, 4)
    print("Rectangle area:", rectangle.area())
    print("Rectangle perimeter:", rectangle.perimeter())

    circle = Circle(3)
    print("Circle area:", circle.area())
    print("Circle circumference:", circle.perimeter())
