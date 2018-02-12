"""Check to see if a given tree is a Binary Search Tree"""


""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
#Set global list to to put all the elements in the tree
stack = []

#Checks if a tree is a BST
def checkBST(root):
    #Call function to populate stack by doing Inorder Traversal
    makeStack(root)
    #Create holder var to iterate over the stack
    holder = stack[0]
    #Create list to place numbers in to check if they're not repeated
    repeats = []
    for i in stack:
        #Check if number is in order
        if i < holder:
            return False
        holder = i
        #Check if number is not repeated
        if i not in repeats:
            repeats.append(i)
        else:
            return False
    return True

#Do inorder traversal and populate stack
def makeStack(root):
    global stack
    if root.left != None:
        makeStack(root.left)
    stack.append(root.data)
    if root.right != None:
        makeStack(root.right)
