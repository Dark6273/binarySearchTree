class TreeNode:
    """TreeNode
        create node
    """
    def __init__(self, value: int, left=None, right=None) -> None:
        """initialize
            initialize node add set value
        Args:
            value (int): integer value
            left (TreeNode, optional): set left child. Defaults to None.
            right (TreeNode, optional): set right child. Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right
    
    def addLeftChild(self, value: int):
        """add left child

        Args:
            value (int): integer value
        """
        self.left = TreeNode(value)
        return self.left
    
    def addRightChild(self, value: int):
        """add right chile

        Args:
            value (int): integer value
        """
        self.right = TreeNode(value)
        return self.right

    def __repr__(self):
        return "value of node equals by -> " + str(self.value)
        