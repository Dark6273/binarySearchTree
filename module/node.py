class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    def printTree(self):
        if self.left:
            self.left.printTree()
            print(self.value)
        if self.right:
            self.right.printTree()