# implementation of a stack using list 

# class Stack:
#     def __init__(self):
#         self.s = []
#     def push(self,val):
#         self.s.append(val)
        
#     def pop(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.s.pop()
    
#     def is_empty(self):
#         return len(self.s) == 0
    
#     def size(self):
#         return len(self.s)
    
#     def peek(self):
#         if self.is_empty():
#             return "stack is empty"
#         return self.s[-1]
# st = Stack()       
# st.push(10)
# st.push(20)
# st.push(30)
# print(st.is_empty())
# print(st.peek())
# st.pop()
# print(st.peek())

class StackWithTop:
    def __init__(self,size):
        self.size = size
        self.top = -1
        self.s = [None] * self.size
    
    def push(self,val):
        if self.top == self.size - 1:
            return "Stack is empty"
        self.top += 1
        self.s[self.top] = val
    
    def is_empty(self):
        return self.top == -1
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        val = self.s[self.top]
        self.top -= 1
        return val
    
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.s[self.top]
    
    def size(self):
        return self.top + 1

st = StackWithTop(5)       
st.push(10)
st.push(20)
st.push(30)
print(st.is_empty())
print(st.peek())
st.pop()
print(st.peek())

