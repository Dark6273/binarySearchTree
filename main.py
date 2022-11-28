from module.tree import Tree
from module.node import TreeNode


def compareTwoTree(tree1: Tree, tree2: Tree):
    """compare two tree
        Comparison of two binary trees

    Args:
        tree1 (Tree): tree for get all node and compare with another tree node
        tree2 (Tree): tree for get all node and compare with another tree node
        
    Return:
        boolean: The sameness of two trees
    """
    def compareTwoNode(node1, node2):
        if node1.value == node2.value:
            if node1.left != None and node2.left != None:
                compareTwoNode(node1.left, node2.right)
            if node1.right != None and node2.right != None:
                compareTwoNode(node1.right, node2.right)
            if (node1.right != None and node2.right == None) or (node1.right == None and node2.right != None): 
                return False
            if (node1.left != None and node2.left == None) or (node1.left == None and node2.left != None): 
                return False
            
            return True
        else:
            return False
    return compareTwoNode(tree1.root, tree2.root)


def main():
    # ** first method **
    # numbers = []
    
    # print("enter numbers add the tree, enter -1 finish number :)")
    
    # while True:
    #     number = int(input("enter a number -> "))
    #     if number == -1:
    #         break
    #     numbers.append(number)
    
    # tree = Tree(numbers)
    # tree.drawGraphicalTree()
    
    # ** second method **
    # numbers = []
    # for i in range(1, 30):
    #     numbers.append(i)
    
    # tree1 = Tree(numbers)
    # tree1.drawGraphicalTree()
    
    # ** third method **
    root = TreeNode(5)
    rR = root.addRightChild(2)
    lR = root.addLeftChild(3)
    lR.addLeftChild(2)
    lR.addRightChild(8)
    rR.addRightChild(6)
    rR.addLeftChild(16)
    
    tree = Tree(root)
    tree.drawGraphicalTree()
    

    
if __name__ == '__main__':
    main()
