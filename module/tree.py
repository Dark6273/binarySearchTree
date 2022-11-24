from turtle import Turtle, mainloop
from module.node import TreeNode

class Tree:
    def __init__(self, data):
        self.data = data
        self.root = self._branching(data)
        
    def _branching(self, data):
        if len(data) == 0:
            return None
        
        nodes = [TreeNode(node) for node in data]
        
        branches = nodes[::-1]
        root = branches.pop()
        
        for node in nodes:
            if branches == []:
                break
            if node:
                if branches: node.left  = branches.pop()
                if branches: node.right = branches.pop()
                
        return root


    def _height(self, root):
        return 1 + max(self._height(root.left), self._height(root.right)) if root else -1
    
    def _jumpTo(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        
    def _draw(self, node, x, y, move):
        if node:
            self.turtle.goto(x, y)
            self._jumpTo(x, y-20)
            self.turtle.write(node.value, align='center', font=('Arial', 12, 'normal'))
            self._draw(node.left, x-move, y-60, move/2)
            self._jumpTo(x, y-20)
            self._draw(node.right, x+move, y-60, move/2)
                
    def drawGraphicalTree(self):
        self.turtle = Turtle()
        self.turtle.speed(0)
        h = self._height(self.root)
        self._jumpTo(0, 30*h)
        self._draw(self.root, 0, 30*h, 40*h)
        self.turtle.hideturtle()
        mainloop()
    
    def countOfNodes(self):
        return len(self.data)
    
    def getHeight(self):
        return self._height(self.root)
    
    def _height(self, root):
        if root is None:
            return 0 
        left = self._height(root.left)
        right = self._height(root.right)
        return max(left, right) + 1
    
    def getCountOfChild(self):
        return self._countOfChild(self.root)
    
    def _countOfChild(self, node):
        if (node == None):
            return 0;
        return (1 + self._countOfChild(node.left) + self._countOfChild(node.right))
    
    def getLeafCount(self):
        return self._LeafCount(self.root)
    
    def _LeafCount(self, node):
        if node is None:
            return 0 
        if(node.left is None and node.right is None):
            return 1 
        else:
            return self._LeafCount(node.left) + self._LeafCount(node.right)
    
    def removeAllNodes(self):
        self.root = None
        self.data = None
        
    def maximum(self):
        return max(self.data)

    def minimum(self):
        return min(self.data)
    
    def _InOrderTraversal(self, status, size ,node):
        if (node == None):
            return;

        self._InOrderTraversal(status, 2*size + 1,node.left);

        status[size] = 1;

        self._InOrderTraversal(status, 2*size + 2,node.right);
    
    
    def _check(self, node):
        if (node == None):
            return True
        
        status = [0 for i in range(0, self.getCountOfChild())]

        self._InOrderTraversal(status, 0, node);

        for i in range(0, self.getCountOfChild()):
            if(status[i] == 0):
                return False
        return True
    
    
    def _search(self, node, key):
        if node is None or node.value == key:
            return node
        
        if node.left != None:
            return self._search(node.left, key)
        if node.right != None:
            return self._search(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)
    
    def checkCompleteTree(self):
        return self._check(self.root)
    
    def drawCommandLine(self):
        self.root.printTree()

    def _compareTwoNode(self, node1, node2):
        if node1.value == node2.value:
            if node1.left != None and node2.left != None:
                self._compareTwoNode(node1.left, node2.right)
            if node1.right != None and node2.right != None:
                self._compareTwoNode(node1.right, node2.right)
            if (node1.right != None and node2.right == None) or (node1.right == None and node2.right != None): 
                return False
            if (node1.left != None and node2.left == None) or (node1.left == None and node2.left != None): 
                return False
            
            return True
        else:
            return False
    
    def compareWithTree(self, tree):
        return self._compareTwoNode(self.root,tree.root)
    
    def _levelOrder(self):
        h = self._height(self.root)
        for i in range(1, h+1):
            self._printCurrentLevel(self.root, i)
    
    def _printCurrentLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.value, end=", ")
        elif level > 1:
            self._printCurrentLevel(root.left, level-1)
            self._printCurrentLevel(root.right, level-1)
    
    def _postOrder(self, node):
        if node:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print(node.value, end=", ")
    
    def _inOrder(self, node):
        if node != None:
            self._inOrder(node.left)
            print(node.value, end=", ")
            self._inOrder(node.right)
        
    def _preOrder(self, node):
        if node != None:
            print(node.value, end=", ")
            self._preOrder(node.left)
            self._preOrder(node.right)
    
    
    def navigation(self, kind):
        kind = kind.lower()
        if kind == "level order" or kind == "levelorder" or kind == "level_order":
            self._levelOrder()
        elif kind == "post order" or kind == "postorder" or kind == "post_order":
            self._postOrder(self.root)
        elif kind == "in order" or kind == "inorder" or kind == "in_order":
            self._inOrder(self.root)
        elif kind == "pre order" or kind == "preorder" or kind == "preOrder":
            self._preOrder(self.root)
        else:
            print("Unknown type")
            exit(-1)
        
        