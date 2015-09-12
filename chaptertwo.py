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

    def deleteDuplicates(self):
        # Array to keep track of all entries.
        previousTable = []
        previous = None
        current = self.head
        while (current):
            previousTable.append(current)
            if (current.get_next() in previousTable):
                previous = current
                current = current.get_next().get_next()
                previous.set_next(current)
            else:
                previous = current
                current = current.get_next()
