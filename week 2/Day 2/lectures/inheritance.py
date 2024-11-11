
#single inheritance
# class GrandPa:
#     def speak(self):
#        print("Grandapa is speaking")
#     def sleep(self):
#         print("Grandpa is sleeping")


# class Parent:
#     def speak(self):
#        print("parent is speaking")
# class Child(Parent):
#     pass
# obj1 = Parent()
# obj1.speak()

# obj2 = Child()
# obj1.speak()
# obj2.sleep()
# obj2.speak()

#multiple inheritance
class GrandPa:
    def speak(self):
       print("Grandapa is speaking")
    def sleep(self):
        print("Grandpa is sleeping")


class Parent:
    def speak(self):
       print("parent is speaking")
class Parent2:
    def speak(self)
        print("Parent 2 is speaking")
class Child(Parent):
    pass
obj1 = Parent()
obj1.speak()

obj2 = Child()
obj1.speak()
obj2.sleep()
obj2.speak()

class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)

nc = NewCircle(1)
print(nc.diameter)

nc.grow()

print(nc.diameter)