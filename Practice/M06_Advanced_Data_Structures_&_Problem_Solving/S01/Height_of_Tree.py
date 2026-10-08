class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def height(root):
    if root is None:
        return -1
    Left_height = height(root.left)
    Right_height = height(root.right)
    return 1 + max(Left_height, Right_height)

def check_height(root):
    if root is None:
        return 0
    Lh = check_height(root.left)
    if Lh == -1:
        return -1
    Rh = check_height(root.right)
    if Rh == -1:
        return -1
    return 1 + max(Lh,Rh)
def is_balanced(root):
    if root is None:
        return True
    left = height(root.left)
    right = height(root.right)
    if abs(left - right) >1:
        return False
    return True

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.left = Node(80)
root.left.left.left.left = Node(100)
root.right.right = Node(60)
print("Height of the Tree is :",height(root))
print()
print("height is :",check_height(root))
print()
print("Balance of Tree :",is_balanced(root))