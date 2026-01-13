class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, curr, data):
        if curr == None:
            return Node(data)
        
        if curr.data == data:
            return curr

        if data < curr.data:
            curr.left = self._insert(curr.left, data)
        else:
            curr.right = self._insert(curr.right, data)

        return curr
    
    def search(self, data):
        def Search(root, data):
            if root == None:
                print("Element Not Found")
                return
                
            if root.data == data:
                print("Element Found")
                return
            
            if data < root.data:
                Search(root.left, data)
            else:
                Search(root.right, data)
        
        Search(self.root, data)
            
    def preorder(self):
        def PreOrder(root):
            if root:
                print(root.data, end=" ")
                PreOrder(root.left)
                PreOrder(root.right)
            
        PreOrder(self.root)
        
    def inorder(self):
        def InOrder(root):
            if root:
                InOrder(root.left)
                print(root.data, end=" ")
                InOrder(root.right)

        InOrder(self.root)
        
    def postorder(self):
        def PostOrder(root):
            if root:
                PostOrder(root.left)
                PostOrder(root.right)
                print(root.data, end=" ")

        PostOrder(self.root)
        
        
        
BST = BinarySearchTree()

e = [10, 5, 15, 3, 8, 12, 19, 25, 30, 8, 2, 11]

for i in e:
    BST.insert(i)

BST.preorder()
print()
BST.inorder()
print()
BST.postorder()
print()
BST.search(19)
BST.search(99)