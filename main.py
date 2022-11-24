from module.tree import Tree


def compareTwoTree(tree1, tree2):
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
    # numbers = []
    
    # print("enter numbers add the tree, enter -1 finish number :)")
    
    # while True:
    #     number = int(input("enter a number -> "))
    #     if number == -1:
    #         break
    #     numbers.append(number)
    
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18]
    
    tree = Tree(numbers)
    tree.drawGraphicalTree()

    
if __name__ == '__main__':
    main()
