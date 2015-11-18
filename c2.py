__author__ = 'derekchiu'

from ll import *

# Remove all duplicates
def removeDups(llnode):
    if llnode == None:
        return False
    current = llnode.head
    # Assume their numbers in the linked list
    # If not the end of the line.
    while current != None:
        runner = current
        # IF Not a duplicate
        while runner.getNext() != None:
            if runner.getNext().getData() == current.getData():
                runner.setNext(runner.getNext().getNext())
        # IF IT IS A DUPLICATE
            else:
                runner.setNext(runner.getNext())
        current = current.getNext()

# Find the kth to last element in linked list.
def removek(ll, k):
    if ll == None:
        return False
    current = ll.head
    # size adjusted from k
    size = ll.size() - k
    index = 0
    while current != None:
        if index == size:
            return current.getData()
        index += 1
        current = current.getNext()

# Remove the middle node of the LinkedList
def removeMiddle(middle):
    if middle == None or middle.getNext() == None:
        return False
    nextNode = middle
    middle.setData(nextNode.getNext().getData())
    middle.getNext(nextNode.getNext())

# Partition LinkedList around x
def partition(node, x):
    bs = None
    be = None
    afterS = None
    ae = None

    while node != None:
        nextnode = node.getNext()
        node.setNext(None)
        if node.getData() < x:
            if bs == None:
                bs = node
                be = bs
            else:
                be.setNext(node)
                be = node
        else:
            if afterS == None:
                afterS = node
                ae = afterS
            else:
                ae.setNext(node)
                ae = node
        node = nextnode
    if bs == None:
        return afterS
    be.setNext(afterS)
    return be

# Add numbers
s =