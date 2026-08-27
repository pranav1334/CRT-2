# class Example:
#     x = 100

#     def display(self):
#         print("this is example class display method")

# obj = Example()
# obj.display()
# print(obj.x)

from math import pi
class Circle:
    r = 7
    def Area(self):
        return pi*self.r*self.r
    def perimeter(self):
        return 2*pi*self.r

c = Circle()
print(c.Area())
print(c.perimeter())    
print(dir(c))
