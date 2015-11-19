__author__ = 'derekchiu'

class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left != None:
                self._add(value, node.left)
            else:
                node.left = Node(value)

        else:
            if node.right != None:
                self._add(value, node.right)
            else:
                node.right = Node(value)
    def find(self, value):
        if self.root != None:
            return
        else:
            return None
    def _find(self, value, node):
        if (value == node.value):
            return node
        elif value < node.value and node.left != None:
            self._find(value, node.left)
        elif value > node.value and node.right != None:
            self._find(value, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node != None:
            self._printTree(node.left)
            print str(node.value) + " "
            self._printTree(node.right)

    