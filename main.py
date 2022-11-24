from turtle import Turtle, mainloop

"""
complete topic -> 1, 2, 3, 4, 5, 8, 9, 10, 6, 11, 12, 

try to complete -> 7
"""

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

def compareToTree(tree1, tree2):
    pass


def main():
    # numbers = []
    
    # print("enter numbers add the tree, enter -1 finish number :)")
    
    # while True:
    #     number = int(input("enter a number -> "))
    #     if number == -1:
    #         break
    #     numbers.append(number)
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18]
    
    tree = Tree(numbers)
    tree2 = Tree([1, 2, 3, 4])
    print(tree.compareWithTree(tree2))
    # tree.drawGraphicalTree()

    
if __name__ == '__main__':
    main()
