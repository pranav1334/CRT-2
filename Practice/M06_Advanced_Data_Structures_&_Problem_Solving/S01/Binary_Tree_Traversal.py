class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
root = Node(1)
root.right = Node(2)
root.left = Node(3)
root.left.right = Node(4)
root.left.right = Node(5)

def Pre_order(root):
    if root:
        print(root.data,end=" -> ")
        Pre_order(root.left)
        Pre_order(root.right)
print("\n Pre_Order Traversal")    
Pre_order(root)

def In_Order(root):
    if root:
        In_Order(root.left)
        print(root.data,end = " -> ")
        In_Order(root.right)
print("\n In_Order Traversal")
In_Order(root)

def Post_order(root):
    if root:
        Post_order(root.left)
        Post_order(root.right)
        print(root.data,end = " ->")
print("\n Post_Order Traversal")
Post_order(root)



from collections import deque
def Level_Order(root):
    if root is None:
        return
    d = deque([root])
    while d:
        node = d.popleft()
        print(node.data,end = " -> ")
        if node.left:
            d.append(node.left)
        if node.right:
            d.append(node.right)


print("\n Level_Order Traversal")
Level_Order(root)
