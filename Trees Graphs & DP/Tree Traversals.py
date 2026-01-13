class Node:
    def __init__(self, data: int):
        self.left = None
        self.data = data
        self.right = None
        

def PreOrder(root):
    if (root != None):
        print(root.data, end=' , ')
        PreOrder(root.left)
        PreOrder(root.right)
        
def InOrder(root):
    if (root != None):
        InOrder(root.left)
        print(root.data, end=' , ')
        InOrder(root.right)
        
def PostOrder(root):
    if (root != None):
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data, end=' , ')
        

TreeRoot = Node(10)
Left = TreeRoot.left = Node(5)
Right = TreeRoot.right = Node(15)
Left.left = Node(3)
Left.right = Node(8)
Right.left = Node(12)
Right.right = Node(19)


print("\nPreOrder Traversal:")
PreOrder(TreeRoot)
print("\nInOrder Traversal:")
InOrder(TreeRoot)
print("\nPostOrder Traversal:")
PostOrder(TreeRoot)
