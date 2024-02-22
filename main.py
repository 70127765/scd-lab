# Define the Shape class with abstract methods area() and perimeter()
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Define Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width
    
    def perimeter(self):
        return 2 * (self._length + self._width)

# Define Circle class inheriting from Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self._radius

# Function to calculate total area of shapes
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

# Function to calculate total perimeter of shapes
def total_perimeter(shapes):
    total = 0
    for shape in shapes:
        total += shape.perimeter()
    return total

# Main function
if __name__ == "__main__":
    # Create instances of shapes
    rectangle = Rectangle(5, 4)
    circle = Circle(3)

    # Display individual properties
    print("Rectangle area:", rectangle.area())
    print("Rectangle perimeter:", rectangle.perimeter())
    print("Circle area:", circle.area())
    print("Circle circumference:", circle.perimeter())

    # Demonstrate polymorphism
    shapes = [rectangle, circle]
    print("Total area of shapes:", total_area(shapes))
    print("Total perimeter of shapes:", total_perimeter(shapes))
