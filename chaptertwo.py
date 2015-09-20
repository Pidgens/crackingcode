__author__ = 'Derek Chiu'

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self, new_node):
        self.next_node = new_node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if (current.get_data() == data):
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in the list")
        return current
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if (current.get_data == data):
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next)

# Using a buffer.
def deleteDuplicatesBuffer(linkedlist):
    # Array to keep track of all entries.
    previousTable = []
    previous = None
    current = linkedlist.head
    while (current):
        previousTable.append(current)
        if (current.get_next() in previousTable):
            previous = current
            current = current.get_next().get_next()
            previous.set_next(current)
        else:
            previous = current
            current = current.get_next()

# Without a buffer - Use a runner.
def deleteDuplicates(linkedlist):
    previous = None
    current = linkedlist.head
    while (current):
        runner = linkedlist.head
        while (runner != current):
            if (runner.get_data() == current.get_data()):
                tmp = current.get_next
                previous.set_next(tmp)
                break
            runner = runner.get_next()
        if (runner == current):
            previous = current
            current = current.get_next()

# Find the n'th last element of a singly linked list.
def findnthElement(linkedlist, n):
    p1 = linkedlist.head
    p2 = linkedlist.head
    for i in range(0,n):
        if (p2 == None):
            # Because size < n
            return None
        p2 = p2.get_next()
    # Do this by - set p2 to n out of the size of linked list
    # Then is essentially size - n and p1 moves with it
    while (p2.get_next is not None):
        p2 = p2.get_next()
        p1 = p1.get_next()
    return p1

# Delete node given only that node.
def deleteMiddle(n):
    next = n.get_next()
    n.data = next.get_data()
    n.get_next = next.get_next()
