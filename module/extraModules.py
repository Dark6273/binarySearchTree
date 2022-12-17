from module.tree import Tree
from module.node import TreeNode


def mathOperationOfTwoTree(tree1: Tree, tree2: Tree, operation: str = "+"):
    def mathOperationOfNode(node1: TreeNode, node2: TreeNode, operation):
        if node1 is not None and node2 is not None:
            if operation == "+":
                node1.value += node2.value
            elif operation == "-":
                node1.value -= node2.value
            elif operation == "*":
                node1.value *= node2.value
            elif operation == "/":
                node1.value /= node2.value
            else:
                return -1

            if node1.right is None and node2.right is not None:
                node1.addRightChild(0 if operation in ("-", "+", "/") else 1)
                mathOperationOfNode(node1.right, node2.right, operation)
            if node1.left is None and node2.left is not None:
                node1.addLeftChild(0 if operation in ("-", "+", "/") else 1)
                mathOperationOfNode(node1.left, node2.left, operation)

    mathOperationOfNode(tree1.root, tree2.root, operation)
