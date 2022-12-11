from module.tree import Tree
from random import randint
from os import name, system
from colorama import Fore
import pyfiglet
from time import sleep


trees = list()


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


def createTree(status: bool) -> Tree:
    if status:
    # ** first method **
        numbers = []

        print("enter numbers add the tree, enter -1 finish number :)")

        while True:
            number = int(input("enter a number -> "))
            if number == -1:
                break
            numbers.append(number)

        tree = Tree(numbers)

    # ** second method **
    else:
        numbers = []
        for i in range(1, 20):
            numbers.append(randint(0, 100))

        tree = Tree(numbers)

    print("inOrder of new tree -> ", end=" ")
    tree.traversal("in order")
    print()
    return tree


def showTrees():
    print(Fore.LIGHTBLUE_EX + "  ------> " + Fore.WHITE + " Trees " + Fore.LIGHTBLUE_EX + " <------")
    for index, tree in enumerate(trees):
        print(Fore.LIGHTBLUE_EX + f" [{index}] " + Fore.WHITE + f"root: {tree.root.value}")
    print()


def show():
    system("cls" if name == "nt" else "clear")
    print(Fore.LIGHTRED_EX + pyfiglet.figlet_format(" B S T ", font="alligator2"))
    sleep(0.03)
    showTrees()
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + "  ------> " + Fore.WHITE + " Select an item " + Fore.LIGHTGREEN_EX + " <------")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [1]" + Fore.WHITE + " Create new tree")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [2]" + Fore.WHITE + " Graphic display")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [3]" + Fore.WHITE + " Count of nodes")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [4]" + Fore.WHITE + " Get height")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [5]" + Fore.WHITE + " Count of Chiled")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [6]" + Fore.WHITE + " Count of leaf")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [7]" + Fore.WHITE + " Remove all nodes")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [8]" + Fore.WHITE + " Traversal")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [9]" + Fore.WHITE + " Compelete tree")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [10]" + Fore.WHITE + " Search")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [11]" + Fore.WHITE + " Compare two tree")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [12]" + Fore.WHITE + " Maximum and minimum")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [13]" + Fore.WHITE + " Add new node")
    sleep(0.03)
    print(Fore.RED + " [14]" + Fore.WHITE + " exit")
    sleep(0.03)  # 0.03s sleep
    try:
        return int(input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + f"Binary Search Tree " + Fore.GREEN + "<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "#" + Fore.RED + "] " + Fore.RESET))
    except:
        return -1


def selectInput(text=None):
    sleep(0.03)  # 0.03s sleep
    return input(
            Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + f"Binary Search Tree " + Fore.GREEN + "<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED + "] " + Fore.LIGHTYELLOW_EX + text + Fore.GREEN + ">> " + Fore.RESET)


def showResult(text=None):
    sleep(0.03)  # 0.03s sleep
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + f"Binary Search Tree " + Fore.GREEN + "<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + ":)" + Fore.RED + "] " + Fore.LIGHTGREEN_EX + text)
    sleep(3)


def traversal():
    print(Fore.LIGHTGREEN_EX + " [1]" + Fore.WHITE + " LevelOrder")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [2]" + Fore.WHITE + " PostOrder")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [3]" + Fore.WHITE + " InOrder")
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + " [4]" + Fore.WHITE + " PreOrder")
    sleep(0.03)
    return int(selectInput("enter number"))


def selection():
    global trees
    while True:
        select = show()
        if select == 1:
            if selectInput("Create random tree (y/yes) ").lower() != "y":
                status = True
            else:
                status = False
            trees.append(createTree(status))
            showResult("create tree successfully!")
        elif select == 14:
            showResult("Good Bye")
            exit(-1)
        else:
            treeNumber = int(selectInput("enter number of tree "))
            if select == 2:
                try:
                    showResult("Drawing graghical tree")
                    trees[treeNumber].drawGraphicalTree()
                except Exception as e:
                    pass
            elif select == 3:
                showResult("Count of Nodes: " + str(trees[treeNumber].countOfNodes()))
            elif select == 4:
                showResult("Height: " + str(trees[treeNumber].getHeight()))
            elif select == 5:
                showResult("Count of Chiledren: " + str(trees[treeNumber].getCountOfChild()))
            elif select == 6:
                showResult("Count of leaf: " + str(trees[treeNumber].getCountOfLeaf()))
            elif select == 7:
                trees[treeNumber].removeAllNodes()
                showResult("Remove all nodes successfully")
            elif select == 8:
                trees[treeNumber].traversal(traversal())
                sleep(5)
            elif select == 9:
                showResult("tree is compelte: " + str(trees[treeNumber].checkCompleteTree()))
            elif select == 10:
                search = int(selectInput("enter of value node"))
                showResult(str(trees[treeNumber].search(search)))
            elif select == 11:
                otherTreeNumber = int(selectInput("enter number of other tree"))
                showResult("Compare two tree is: " + str(trees[treeNumber].compareWithTree(trees[otherTreeNumber])))
            elif select == 12:
                if selectInput("maximum -> 1 and minimum -> 2").lower() == "1":
                    showResult("Maximum value: " + str(trees[treeNumber].maximum()))
                else:
                    showResult("Minimum value: " + str(trees[treeNumber].minimum()))
            elif select == 13:
                trees[treeNumber].insert(int(selectInput("enter value of new node ")))
                showResult("add new node successfully!")
            else:
                showResult("wrong input")


def main():
    selection()


if __name__ == '__main__':
    main()
