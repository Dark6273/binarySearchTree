from turtle import Turtle, mainloop, title, Screen, bye
from module.node import TreeNode


class Tree:
    """binary tree class
        A binary tree is a data structure in which each node 
        has at most two children. The logical representation 
        of the above tree is given below: In the above tree, 
        node 1 contains two pointers, i.e., left and a right 
        pointer pointing to the left and right node respectively.
    """

    def __init__(self, data: list or TreeNode) -> None:
        """__init__
            initialize data and create nodes

        Args:
            data (list): list of numbers for create a child
        """
        self.data = data
        self.root = None
        if type(data) == list:
            for number in data:
                self._branching(self.root, number)
        elif type(data) == TreeNode:
            self.root = data
        else:
            print("wrong input type -> allowed types (list[numbers], TreeNode), entered type -> {}".format(type(data)))
            exit(-1)

    def _branching(self, node: TreeNode, data: int) -> None:
        """_branching
            Calculation of the children of each branch
        Args:
            data (list): list of numbers for create a child
        Returns:
            root (TreeNode): main branch
        """
        if self.root == None:
            self.root = TreeNode(data)
        else:
            if node.value > data:
                if node.left != None:
                    self._branching(node.left, data)
                else:
                    node.addLeftChild(data)
            elif node.value < data:
                if node.right != None:
                    self._branching(node.right, data)
                else:
                    node.addRightChild(data)
            elif node.value == data:
                print("you can't insert duplicate value")
                return -1

    def insert(self, value: int) -> None:
        if self._branching(self.root, value) != -1:
            return False
        return True

    def _jumpTo(self, x: int, y: int) -> None:
        """_jumpTo
            Moving the pen and placing it in the right place 

        Args:
            x (int): Coordinates in the horizontal plane
            y (int): Coordinates in the vertical plane
        """
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()

    def _draw(self, node: TreeNode, x: int, y: int, move: int) -> None:
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
            self._jumpTo(x, y - 20)
            self.turtle.begin_fill()
            self.turtle.circle(12)
            self.turtle.end_fill()
            self.turtle.color('white')
            self.turtle.write(node.value, align='center', font=('Arial', 11, 'bold'))
            self.turtle.color('black')
            self._draw(node.left, x - move, y - 60, move / 2)
            self._jumpTo(x, y - 20)
            self._draw(node.right, x + move, y - 60, move / 2)

    def drawGraphicalTree(self) -> None:
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
        self.turtle.write("Graphical Binary Tree - Mahdi Khosravi, 40007583 :)", align="center",
                          font=('Arial', 17, "bold"))
        self.turtle.speed(0)
        h = self._height(self.root)
        self._jumpTo(0, 30 * h)
        self._draw(self.root, 0, 30 * h, 40 * h)
        self.turtle.hideturtle()
        try:
            mainloop()
        except:
            bye()
        bye()

    def countOfNodes(self) -> int:
        """count of nodes

        Returns:
            int: count of nodes
        """

        def _countOfNodes(node, counter=0) -> int:
            if node:
                counter += 1
                counter = _countOfNodes(node.right, counter)
                counter = _countOfNodes(node.left, counter)
            return counter

        return _countOfNodes(self.root)

    def getHeight(self) -> int:
        """get height
        
        Returns:
            int: height size
        """
        return self._height(self.root)

    def _height(self, root: TreeNode) -> int:
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

    def getCountOfChild(self) -> int:
        """get count of children

        Returns:
            int: Number of children
        """

        def _countOfChild(node: TreeNode) -> int:
            if (node == None):
                return 0;
            return (1 + _countOfChild(node.left) + _countOfChild(node.right))
        return _countOfChild(self.root)

    def getCountOfLeaf(self) -> int:
        """get count of leaf

        Returns:
            int: number of leaf
        """
        def _countOfLeaf(node: TreeNode) -> int:
            if node is None:
                return 0
            if (node.left is None and node.right is None):
                return 1
            else:
                return _countOfLeaf(node.left) + _countOfLeaf(node.right)

        return _countOfLeaf(self.root)

    def removeAllNodes(self) -> bool:
        """remove all nodes
            Remove the original node
        """
        self.root = None
        self.data = None
        return True

    def maximum(self) -> int:
        """maximum
            Calculate maximum number in binary tree

        Returns:
            int: maximum value
        """

        def _maximum(node: TreeNode, max: int) -> int:
            if node:
                if node.value > max:
                    max = node.value
                if node.right != None:
                    max = _maximum(node.right, max)
                else:
                    max = _maximum(node.left, max)
            return max
        return _maximum(self.root, self.root.value)

    def minimum(self) -> int:
        """minimum
            Calculate minimum number in binary tree

        Returns:
            int: minimum value
        """

        def _minimum(node: TreeNode, min: int) -> int:
            if node:
                if node.value < min:
                    min = node.value
                if node.left != None:
                    min = _minimum(node.left, min)
                else:
                    min = _minimum(node.right, min)
            return min
        return _minimum(self.root, self.root.value)

    def _inOrderTraversal(self, status: int, size: int, node: TreeNode) -> None:
        """_inOrderTraversal
            Check for navigability

        Args:
            status (int): default status of child -> 0 -> mean empty
            node (TreeNode): TreeNode for check exist
            size (int): None
        """
        if (node == None):
            return;

        self._inOrderTraversal(status, 2 * size + 1, node.left);

        status[size] = 1;

        self._inOrderTraversal(status, 2 * size + 2, node.right);

    def search(self, key: int) -> TreeNode:
        """search
            Checking for the existence of this particular value in the tree
            
        Args:
            key (int): desired key

        Returns:
            TreeNode: The carrier node of the desired value
        """

        def _search(node: TreeNode, key: int) -> TreeNode:
            if node is None or node.value == key:
                return node

            if node.value > key:
                return _search(node.left, key)
            elif node.value < key:
                return _search(node.right, key)
        return _search(self.root, key)

    def checkFullTree(self) -> bool:
        """check complete tree
            Checking the completeness of the tree

        Returns:
            boolean: Is it complete or not?
        """

        def _checkFullTree(node: TreeNode) -> bool:
            queue = list()
            queue.append(node)

            while queue != []:
                temp = queue.pop()

                if temp.left == None and temp.right == None:
                    continue
                elif temp.right != None and temp.left != None:
                    queue.append(temp.right)
                    queue.append(temp.left)
                else:
                    return False
            return True
        return _checkFullTree(self.root)

    def isComplete(self):
        def _isComplete(node: TreeNode, index: int, nodeCount: int) -> bool:
            if node == None:
                return True
            if index >= nodeCount:
                return False
            return self._isComplete(node.left, 2 * index + 1, nodeCount) and self._isComplete(node.right, 2 * index + 2,
                                                                                              nodeCount)

        return _isComplete(self.root, 0, self.countOfNodes())

    def _compareTwoNode(self, node1: TreeNode, node2: TreeNode) -> bool:
        """_compareTwoNode
            Checking the existence of two nodes and their amount

        Args:
            node1 (TreeNode): node for check value
            node2 (TreeNode): node for check value

        Returns:
            boolean: Comparison of two node
        """
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return False

        if self._compareTwoNode(node1.right, node2.right) and self._compareTwoNode(node1.left, node2.left) and node2.value == node1.value:
            return True
        return False

    def compareWithTree(self, tree: TreeNode) -> bool:
        """compare with another tree

        Args:
            tree (TreeNode): Tree to compare all nodes
            
        Returns:
            boolean: Comparison with another tree
        """
        return self._compareTwoNode(self.root, tree.root)

    def _levelOrder(self) -> None:
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

    def _printCurrentLevel(self, root: TreeNode, level: int) -> None:
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
            self._printCurrentLevel(root.left, level - 1)
            self._printCurrentLevel(root.right, level - 1)

    def _postOrder(self, node: TreeNode) -> None:
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

    def _inOrderRecursion(self, node: TreeNode) -> None:
        """_inOrderRecursion
            In order tree traversal is a way of traversing a binary 
            search tree in non-decreasing order. To get nodes of 
            BST in non-increasing order, a variation of InOrder 
            traversal where InOrder traversal is reversed can be used.

        Args:
            node (TreeNode): node for show value
        """
        if node != None:
            self._inOrderRecursion(node.left)
            print(node.value, end=", ")
            self._inOrderRecursion(node.right)

    def _inOrder(self) -> None:
        """_inOrder
            In order tree traversal is a way of traversing a binary
            search tree in non-decreasing order. To get nodes of
            BST in non-increasing order, a variation of InOrder
            traversal where InOrder traversal is reversed can be used.
        """
        numbers = list()

        node = self.root

        while True:
            if node is not None:
                numbers.append(node)
                node = node.left
            elif numbers:
                node = numbers.pop()
                print(node.value, end=", ")
                node = node.right
            else:
                break

    def _preOrder(self, node: TreeNode) -> None:
        """_preOrderRecursion
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

    def traversal(self, kind: str, recursive: bool = True) -> None:
        """traversal
            There are three common ways to traverse a tree in 
            depth-first order: in-order, pre-order, and post-order. 

        Args:
            kind (str): Specify the type of navigation
        """
        if kind == "level order" or kind == "levelorder" or kind == "level_order" or kind == 1:
            self._levelOrder()
        elif kind == "post order" or kind == "postorder" or kind == "post_order" or kind == 2:
            self._postOrder(self.root)
        elif kind == "in order" or kind == "inorder" or kind == "in_order" or kind == 3:
            return self._inOrderRecursion(self.root) if recursive else self._inOrder()
        elif kind == "pre order" or kind == "preorder" or kind == "preOrder" or kind == 4:
            self._preOrder(self.root)
        else:
            print("Unknown type - navigation")
            exit(-1)
        print()
