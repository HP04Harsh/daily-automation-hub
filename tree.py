class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)
root.left.right = Node(50)

def printTree(root):
    if root is None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

printTree(root)    