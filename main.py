from module.tree import Tree
from random import randint


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
    numbers = []
    for i in range(1, 20):
        numbers.append(randint(0, 100))
    
    tree1 = Tree(numbers)
    print(tree1.getCountOfLeaf())
    # tree1.drawGraphicalTree()
    tree1.traversal("pre order")
    print()
    tree1.traversal("pre order", recursive=False)


if __name__ == '__main__':
    main()
