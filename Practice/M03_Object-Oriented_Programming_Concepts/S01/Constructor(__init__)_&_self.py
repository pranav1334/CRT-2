from math import pi
class Circle:
    r = 7
    count = 0   
    def __init__(self):
        self.count += 1
    def Area(self):
        return pi*self.r*self.r
    def perimeter(self):
        return 2*pi*self.r

c1 = Circle()
c2 = Circle()
c3 = Circle()
print(c1.Area())
