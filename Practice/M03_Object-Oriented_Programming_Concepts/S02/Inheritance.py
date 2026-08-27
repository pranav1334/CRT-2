'''
inheritance : acquring properties and from one class to another class

types of inheritiance:

1. single inheritance
2. multiple inheritance
3. multilevel inheritance
4. hierarchical inheritance
5. hybrid inheritance
'''

# single inheritance

# class A:
#     def displayA(self):
#         print("this is class A method")

# class B(A):
#     def displayB(self):
#         print("this is class B method")

# obj = B()
# obj.displayA()
# obj.displayB()

# multi-level inheritance
# class A:
#     def displayA(self):
#         print("this is class A method")    
# class B(A):
#     def displayB(self):
#         print("this is class B method")
# class C(B):
#     def displayC(self):
#         print("this is class C method")


# multiple inheritance
class A:
    def display(self):
        print("this is class A method") 
class B:
    def display(self):
        print("this is class B method")
class C(A,B):
    def displayC(self):
        print("this is class C method")
c = C()
c.display()        
        
# hierarchical inheritance
# class A:
#     def displayA(self):
#         print("this is class A method")
# class B(A):
#     def displayB(self):
#         print("this is class B method")
# class C(A):
#     def displayC(self):
#         print("this is class C method")        
                  