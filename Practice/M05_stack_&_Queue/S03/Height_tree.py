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
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
root.left.left.left = Node(80)
root.left.left.left.left = Node(100)
print("Height of the Tree is :",height(root))