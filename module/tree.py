from turtle import Turtle, mainloop, title, Screen
from module.node import TreeNode

"""binary tree
    Binary tree with methods
        1- graphical show
        2- count of nodes
        3- height
        4- count of child
        5- count of leaf
        6- remove all nodes
        7- maximum and minimum
        8- navigation -> (1- level order, 2- in order, 3- post order, 4- pre order)
        9- complete tree -> boolean result
        10- search
        11- compare two tree
"""

class Tree:
    """binary tree class
        A binary tree is a data structure in which each node 
        has at most two children. The logical representation 
        of the above tree is given below: In the above tree, 
        node 1 contains two pointers, i.e., left and a right 
        pointer pointing to the left and right node respectively.
    """
    
    def __init__(self, data: list):
        """__init__
            initialize data and create nodes

        Args:
            data (list): list of numbers for create a child
        """
        self.data = data
        self.root = self._branching(data)
        
        
    def _branching(self, data):
        """_branching
            Calculation of the children of each branch
        Args:
            data (list): list of numbers for create a child
        Returns:
            root (TreeNode): main branch
        """
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
    
    
    def _jumpTo(self, x: int, y: int):
        """_jumpTo
            Moving the pen and placing it in the right place 

        Args:
            x (int): Coordinates in the horizontal plane
            y (int): Coordinates in the vertical plane
        """
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        
        
    def _draw(self, node: TreeNode, x: int, y: int, move: int):
        """_draw
            Drawing a connecting line between the children and drawing 
            a circle and writing its value

        Args:
            node (TreeNode): TreeNode for get value
            x (int): Coordinates in the horizontal plane
            y (int): Coordinates in the vertical plane
            move (int): Calculation of displacement value
        """
        if node:
            self.turtle.goto(x, y)
            self._jumpTo(x, y-20)
            self.turtle.begin_fill()
            self.turtle.circle(12)
            self.turtle.end_fill()
            self.turtle.color('white')
            self.turtle.write(node.value, align='center', font=('Arial', 11, 'bold'))
            self.turtle.color('black')
            self._draw(node.left, x-move, y-60, move/2)
            self._jumpTo(x, y-20)
            self._draw(node.right, x+move, y-60, move/2)
                
                
    def drawGraphicalTree(self):
        """draw graphical tree
            create turtle page
            set title and page size
            write name of author
            run until close page
        """
        
        self.turtle = Turtle()
        title("Graphical binary tree")
        screen = Screen()
        screen.setup(1024, 700)
        self._jumpTo(0, 250)
        self.turtle.write("Graphical Binary Tree - Mahdi Khosravi, 40007583 :)", align="center", font=('Arial', 17, "bold"))
        self.turtle.speed(0)
        h = self._height(self.root)
        self._jumpTo(0, 30*h)
        self._draw(self.root, 0, 30*h, 40*h)
        self.turtle.hideturtle()
        mainloop()
    
    
    def countOfNodes(self):
        """count of nodes

        Returns:
            int: count of nodes
        """
        return len(self.data)
    
    
    def getHeight(self):
        """get height
        
        Returns:
            int: height size
        """
        return self._height(self.root)
    
    
    def _height(self, root: TreeNode):
        """_height
            Recursive calculation of tree binary height

        Args:
            root (TreeNode): main node

        Returns:
            int: height size
        """
        if root is None:
            return 0 
        left = self._height(root.left)
        right = self._height(root.right)
        return max(left, right) + 1
    
    
    def getCountOfChild(self):
        """get count of children

        Returns:
            int: Number of children
        """
        return self._countOfChild(self.root)
    
    
    def _countOfChild(self, node: TreeNode):
        """_countOfChild
            Calculate the number of tree children recursively
            
        Args:
            node (TreeNode): main node

        Returns:
            int: number of children
        """
        if (node == None):
            return 0;
        return (1 + self._countOfChild(node.left) + self._countOfChild(node.right))
    
    
    def getCountOfLeaf(self):
        """get count of leaf

        Returns:
            int: number of leaf
        """
        return self._countOfLeaf(self.root)
    
    
    def _countOfLeaf(self, node: TreeNode):
        """_countOfLeaf
            Calculating the number of tree leaves recursively

        Args:
            node (TreeNode): main node

        Returns:
            int: number of leaf
        """
        if node is None:
            return 0 
        if(node.left is None and node.right is None):
            return 1 
        else:
            return self._countOfLeaf(node.left) + self._countOfLeaf(node.right)
    
    
    def removeAllNodes(self):
        """remove all nodes
            Remove the original node
        """
        self.root = None
        self.data = None
        
        
    def maximum(self):
        """maximum
            Calculate maximum number in binary tree

        Returns:
            int: maximum value
        """
        return max(self.data)


    def minimum(self):
        """minimum
            Calculate minimum number in binary tree

        Returns:
            int: minimum value
        """
        return min(self.data)
    
    
    def _inOrderTraversal(self, status: int, size: int ,node: TreeNode):
        """_inOrderTraversal
            Check for navigability

        Args:
            status (int): default status of child -> 0 -> mean empty
            node (TreeNode): TreeNode for check exist
            size (int): None
        """
        if (node == None):
            return;

        self._inOrderTraversal(status, 2*size + 1,node.left);

        status[size] = 1;

        self._inOrderTraversal(status, 2*size + 2,node.right);
    
    
    def _check(self, node: TreeNode):
        """_check
            Checking the completeness of the tree

        Args:
            node (TreeNode): main node

        Returns:
            boolean: Is it complete or not?
        """
        if (node == None):
            return True
        
        status = [0 for i in range(0, self.getCountOfChild())]

        self._inOrderTraversal(status, 0, node);

        for i in range(0, self.getCountOfChild()):
            if(status[i] == 0):
                return False
        return True
    
    
    def _search(self, node: TreeNode, key: int):
        """_search
            Checking for the existence of this particular value in the tree

        Args:
            node (TreeNode): node for get value and check with key
            key (int): desired key

        Returns:
            TreeNode: The carrier node of the desired value
        """
        if node is None or node.value == key:
            return node
        
        if node.left != None:
            return self._search(node.left, key)
        if node.right != None:
            return self._search(node.right, key)
    
    
    def search(self, key: int):
        """search
            Checking for the existence of this particular value in the tree
            
        Args:
            key (int): desired key

        Returns:
            TreeNode: The carrier node of the desired value
        """
        return self._search(self.root, key)
    
    
    def checkCompleteTree(self):
        """check complete tree
            Checking the completeness of the tree

        Returns:
            boolean: Is it complete or not?
        """
        return self._check(self.root)
    
    
    def drawCommandLine(self):
        """draw command line -> CLI
            Display data of all nodes
        """
        self.root.printTree()
        

    def _compareTwoNode(self, node1: TreeNode, node2: TreeNode):
        """_compareTwoNode
            Checking the existence of two nodes and their amount

        Args:
            node1 (TreeNode): node for check value
            node2 (TreeNode): node for check value

        Returns:
            boolean: Comparison of two node
        """
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
    
    
    def compareWithTree(self, tree: TreeNode):
        """compare with another tree

        Args:
            tree (TreeNode): Tree to compare all nodes
            
        Returns:
            boolean: Comparison with another tree
        """
        return self._compareTwoNode(self.root,tree.root)
    
    
    def _levelOrder(self):
        """_levelOrder
            Level by level display of tree branches
            
            The level order traversal of a tree is the
            algorithm to process all nodes of a tree
            by traversing through depth, first the
            root, then the child of the root, etc.
        """
        height = self._height(self.root)
        for i in range(1, height + 1):
            self._printCurrentLevel(self.root, i)
    
    
    def _printCurrentLevel(self, root: TreeNode, level: int):
        """_printCurrentLevel
            Show all children level
            
        Args:
            root (TreeNode): node for show value
            level (int): Level number
        """
        if root is None:
            return
        if level == 1:
            print(root.value, end=", ")
        elif level > 1:
            self._printCurrentLevel(root.left, level-1)
            self._printCurrentLevel(root.right, level-1)
    
    
    def _postOrder(self, node: TreeNode):
        """_postOrder
            In post order traversal, the tree is traversed in this way: 
            left, right, root. The algorithm approach is to use the 
            current node's left and right child references to 
            navigate back and forth. This could be faster 
            depending on the tree structure, for example
            in a right-skewed tree.

        Args:
            node (TreeNode): node for show value
        """
        if node:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print(node.value, end=", ")
    
    
    def _inOrder(self, node: TreeNode):
        """_inOrder
            In order tree traversal is a way of traversing a binary 
            search tree in non-decreasing order. To get nodes of 
            BST in non-increasing order, a variation of InOrder 
            traversal where InOrder traversal is reversed can be used.

        Args:
            node (TreeNode): node for show value
        """
        if node != None:
            self._inOrder(node.left)
            print(node.value, end=", ")
            self._inOrder(node.right)
        
        
    def _preOrder(self, node: TreeNode):
        """_preOrder
            PreOrder tree traversal is a depth-first tree traversal algorithm. 
            In depth-first traversal, we start at the root node and then we 
            explore a branch of the tree till the end and then we backtrack 
            and traverse another branch. In the preOrder traversal, first, 
            we traverse the current node, and then we traverse the left 
            child or left subtree of the current node, and then we 
            traverse the right child or right subtree of the 
            current node. We perform this operation 
            recursively till all the nodes are traversed.

        Args:
            node (TreeNode): node for show value
        """
        if node != None:
            print(node.value, end=", ")
            self._preOrder(node.left)
            self._preOrder(node.right)
    
    
    def navigation(self, kind: str):
        """navigation
            There are three common ways to traverse a tree in 
            depth-first order: in-order, pre-order, and post-order. 

        Args:
            kind (str): Specify the type of navigation
        """
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
            print("Unknown type - navigation")
            exit(-1)
        
