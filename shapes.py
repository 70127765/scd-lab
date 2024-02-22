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
    
    # Getter and Setter for length
    def get_length(self):
        return self._length
    
    def set_length(self, length):
        if length > 0:
            self._length = length
        else:
            print("Length must be greater than 0.")

    # Getter and Setter for width
    def get_width(self):
        return self._width
    
    def set_width(self, width):
        if width > 0:
            self._width = width
        else:
            print("Width must be greater than 0.")

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self._radius
    
    # Getter and Setter for radius
    def get_radius(self):
        return self._radius
    
    def set_radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            print("Radius must be greater than 0.")

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(5, 4)
    print("Rectangle area:", rectangle.area())
    print("Rectangle perimeter:", rectangle.perimeter())

    # Using getters and setters
    rectangle.set_length(6)
    rectangle.set_width(3)
    print("Updated Rectangle area:", rectangle.area())
    print("Updated Rectangle perimeter:", rectangle.perimeter())

    circle = Circle(3)
    print("Circle area:", circle.area())
    print("Circle circumference:", circle.perimeter())

    # Using getters and setters
    circle.set_radius(5)
    print("Updated Circle area:", circle.area())
    print("Updated Circle circumference:", circle.perimeter())
