class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, Rectangle):  # Need to modify this for every new shape
                total_area += shape.area()
            elif isinstance(shape, Circle):   # Need to modify this for every new shape
                total_area += shape.area()
        return total_area

# Usage
shapes = [Rectangle(4, 5), Circle(7)]
calculator = AreaCalculator()
print(calculator.calculate_area(shapes))