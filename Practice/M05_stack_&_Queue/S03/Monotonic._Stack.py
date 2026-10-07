#  Monotonic Incressing Stack
#  General pattern 

arr = [4,12,5,3,1,2,5,3,1,2,4,6]
stack = []
for x in arr:
    while stack and stack[-1] > x:
        stack.pop()
    stack.append(x)
    
# Monotonic decressing Stack
# General pattern
stack = []

for x in arr:
    while stack and stack[-1] < x:
        stack.pop()
    stack.append(x)
    
    
    
def NextGresterElement(arr):
    pass