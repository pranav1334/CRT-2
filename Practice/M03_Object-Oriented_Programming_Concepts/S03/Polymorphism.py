'''
Polymorphism:
poly ==> many
morph ==> forms

Tyes of Polymorphism:
1. complile time 
    1. function overloading
    2. operator overloading
2. run time
    1. method overriding
'''

# def add(a,b):
#     return a+b
# def add(a,b,c):
#     return a+b+c    
# def add(a,b,c,d):
#     return a+b+c+d
# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40))

# def add(*values):
#     return sum(values)
# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40))

# operator overloading
# class A:
#     def __init__(self,x):
#         self.x = x
#     def __add__(self,val):
#         return self.x + val.x
#     def __sub__(self,val):
#         return self.x - val.x
#     def __lt__(self,val):
#         return self.x < val.x

# a = A(10)
# b = A(20)
# print(a+b) 
# print(a-b)
# print(a<b)

class B:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,val):
        return (self.x + val.x, self.y + val.y)
    def __sub__(self,val):
        return (self.x - val.x, self.y - val.y)

a = B(10,20)
b = B(30,40)    
print(a+b) 
print(a-b) 

# method overriding : same method name in parent and child class
class Parent:
    def display(self):
        print("this is parent class method")

class Child(Parent):
    def display(self):
        print("this is child class method")

c = Child()
c.display()
Parent.display(c)

# duck typing

class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()   
make_sound(d)
make_sound(c)                    