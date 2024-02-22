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

    # Method to calculate area based on rectangle formula
    def calculate_area(self):
        return self._length * self._width

    # Method to calculate perimeter based on rectangle formula
    def calculate_perimeter(self):
        return 2 * (self._length + self._width)

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

    # Method to calculate area based on circle formula
    def calculate_area(self):
        return math.pi * self._radius ** 2

    # Method to calculate perimeter based on circle formula
    def calculate_perimeter(self):
        return 2 * math.pi * self._radius

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(5, 4)
    print("Rectangle area:", rectangle.calculate_area())
    print("Rectangle perimeter:", rectangle.calculate_perimeter())

    # Using getters and setters
    rectangle.set_length(6)
    rectangle.set_width(3)
    print("Updated Rectangle area:", rectangle.calculate_area())
    print("Updated Rectangle perimeter:", rectangle.calculate_perimeter())

    circle = Circle(3)
    print("Circle area:", circle.calculate_area())
    print("Circle circumference:", circle.calculate_perimeter())

    # Using getters and setters
    circle.set_radius(5)
    print("Updated Circle area:", circle.calculate_area())
    print("Updated Circle circumference:", circle.calculate_perimeter())
class DataProcessor:
    def __init__(self, data):
        self._data = data

    def process_data(self):
        pass

    def get_processed_data(self):
        pass

# Example usage
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    processor = DataProcessor(data)
    processor.process_data()
    processed_data = processor.get_processed_data()
    print("Processed data:", processed_data)
class DataProcessor:
    def __init__(self, data):
        self._data = data

    def sort_data(self):
        if isinstance(self._data, (list, tuple)):
            self._data = sorted(self._data)
        elif isinstance(self._data, dict):
            self._data = dict(sorted(self._data.items()))
        elif isinstance(self._data, set):
            self._data = sorted(self._data)

    def append_data(self, item):
        if isinstance(self._data, list):
            self._data.append(item)
        else:
            print("Cannot append to this data type.")

    def update_data(self, key, value):
        if isinstance(self._data, dict):
            self._data[key] = value
        else:
            print("Cannot update this data type.")

    def remove_data(self, item):
        if isinstance(self._data, list):
            if item in self._data:
                self._data.remove(item)
        elif isinstance(self._data, dict):
            if item in self._data:
                del self._data[item]
        elif isinstance(self._data, set):
            if item in self._data:
                self._data.remove(item)
        else:
            print("Cannot remove from this data type.")

    def get_processed_data(self):
        return self._data

# Example usage
if __name__ == "__main__":
    # List example
    data_list = [3, 1, 4, 2, 5]
    processor_list = DataProcessor(data_list)
    print("Original list:", processor_list.get_processed_data())

    processor_list.sort_data()
    print("Sorted list:", processor_list.get_processed_data())

    processor_list.append_data(6)
    print("Appended list:", processor_list.get_processed_data())

    processor_list.remove_data(4)
    print("List after removing 4:", processor_list.get_processed_data())

    # Dictionary example
    data_dict = {'b': 2, 'a': 1, 'c': 3}
    processor_dict = DataProcessor(data_dict)
    print("\nOriginal dictionary:", processor_dict.get_processed_data())

    processor_dict.sort_data()
    print("Sorted dictionary:", processor_dict.get_processed_data())

    processor_dict.update_data('d', 4)
    print("Dictionary after updating:", processor_dict.get_processed_data())

    processor_dict.remove_data('b')
    print("Dictionary after removing 'b':", processor_dict.get_processed_data())

    # Set example
    data_set = {3, 1, 4, 1, 5}
    processor_set = DataProcessor(data_set)
    print("\nOriginal set:", processor_set.get_processed_data())

    processor_set.sort_data()
    print("Sorted set:", processor_set.get_processed_data())

    processor_set.remove_data(4)
    print("Set after removing 4:", processor_set.get_processed_data())
if __name__ == "__main__":
    # List example
    data_list = [3, 1, 4, 2, 5]
    processor_list = DataProcessor(data_list)
    print("Original list:", processor_list.get_processed_data())

    processor_list.sort_data()
    print("Sorted list:", processor_list.get_processed_data())

    processor_list.append_data(6)
    print("Appended list:", processor_list.get_processed_data())

    processor_list.remove_data(4)
    print("List after removing 4:", processor_list.get_processed_data())

    # Dictionary example
    data_dict = {'b': 2, 'a': 1, 'c': 3}
    processor_dict = DataProcessor(data_dict)
    print("\nOriginal dictionary:", processor_dict.get_processed_data())

    processor_dict.sort_data()
    print("Sorted dictionary:", processor_dict.get_processed_data())

    processor_dict.update_data('d', 4)
    print("Dictionary after updating:", processor_dict.get_processed_data())

    processor_dict.remove_data('b')
    print("Dictionary after removing 'b':", processor_dict.get_processed_data())

    # Set example
    data_set = {3, 1, 4, 1, 5}
    processor_set = DataProcessor(data_set)
    print("\nOriginal set:", processor_set.get_processed_data())

    processor_set.sort_data()
    print("Sorted set:", processor_set.get_processed_data())

    processor_set.remove_data(4)
    print("Set after removing 4:", processor_set.get_processed_data())
git add data_structures.py
git commit -m "Implemented DataProcessor class with methods for data structure operations"
git push origin main
