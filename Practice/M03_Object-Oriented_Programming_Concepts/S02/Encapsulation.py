'''
data hiding :
access specifer
1. public
2. protected
3. private
'''

# class A:
#     a = 10 # public
#     _b = 20 # protected
#     __c = 30 # private

# obj = A()
# print(obj.a) # public   
# print(obj._b) # protected
# print(obj._A__c) # private    

# Access and modify privite members from class using methods

class bank:
    def __init__(self,balance):
        self.__balance = balance # private member
    def credit(self, amount):
        self.__balance += amount
    def debit(self, amount):
        self.__balance -= amount
    def display(self):
        print("Current balance:", self.__balance)

b = bank(1000)
b.display()
b.credit(1500)
b.display()
b.debit(500)
b.display()