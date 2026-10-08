'''
Diameter:Longets path between the nodes
Formula:
current_diameter = (left_height + right_height) + 2
Algorithm:
1. Find the height of left and right subtrees
2. Calculate the diameter at the current node using the formula
3.Find the length of left dia and length of right dia
4. Return the maximum of the three values

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def height(root):
    if root is None:
        return -1
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

def dimeter(root):
    if root is None:
        return -1
    left = height(root.left)
    right = height(root.right)
    curr_dia = left + right + 2
    left_dia = dimeter(root.left)
    right_dia = dimeter(root.right)
    return max(curr_dia, left_dia, right_dia)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.left = Node(80)
root.left.left.left.left = Node(100)
root.right.right = Node(60)
res = dimeter(root)
print("diameter is: ",res)