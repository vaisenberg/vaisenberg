import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius:
            self._radius = radius
        elif diameter:
            self._radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided")

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    def area(self):
        return math.pi * self._radius ** 2

    def __str__(self):
        return f"Circle with radius {round(self.radius)} and diameter {round(self.diameter, 2)}"


c1 = Circle(radius=5)
c2 = Circle(diameter=12)

print(c1)  
print(c2)  
print(f"Area of c1: {round(c1.area(), 2)}")  
print(f"Area of c2: {round(c2.area(), 2)}")  


