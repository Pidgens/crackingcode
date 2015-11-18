__author__ = 'Derek Chiu'

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def insert(self, item):
        # Set temp
        temp = Node(item)
        # Set to next node (First position on list)
        temp.setNext(self.head)
        # Set the inserted node as the head
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, desired):
        current = self.head
        found = False
        # While not found AND not at the end of the list
        while (not found) and current != None:
            if (current.getData() == desired):
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        prev = None
        found = False
        while (not found):
            if (current.getData() == item):
                found = True
            else:
                prev = current
                current = current.getNext()
        if (prev == None):
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())


