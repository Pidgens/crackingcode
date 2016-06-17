####################################################################
####################################################################
####################################################################

from stacks import Stack
maxStack = 2


class SetOfStacks:
    def __init__(self):
        self.currentStack = []
        self.stacks = []
    def push(self, item):
        if len(self.currentStack) < maxStack:
            if len(self.currentStack) == 0:
                self.stacks.append(self.currentStack)
            self.currentStack.append(item)
            return self.stacks
        else:
            self.currentStack = [item]
            self.stacks.append(self.currentStack)
            return self.stacks
    def pop(self):
        return self.currentStack.pop()
    def peek(self):
        return self.currentStack[len(self.currentStack)-1]
    def sizeOfCurrentStack(self):
        return len(self.currentStack)
    def numberOfStacks(self):
        return len(self.stacks)
    def popAtIndex(self, index):
        if index < len(self.stacks):
            return self.stacks[index].pop()
        else:
            return 'NOPE'
    def peekStacks(self):
        return self.stacks

def sortAscendingOrder(s1):
    s2 = Stack()
    while not s1.isEmpty():
        # print 'S2:', s2.stack()
        # print 'S1:', s1.stack()
        last = s1.pop()
        while (not s2.isEmpty() and s2.peek() > last):
            s1.push(s2.pop())
        s2.push(last)
    return s2

class Animal:
    def __init__(self, animal):
        self.type = animal
        self.order = 0

    def getType(self):
        return self.type

    def getOrder(self):
        return self.getOrder()

class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.total = []

    def enqueue(self, animal):
        if animal.getType() == 'dogs':
            self.dogs.append(animal)
        else:
            self.cats.append(animal)
        self.total.append(animal)

    def dequeueAny(self):
        return self.total.pop()

    def dequeueDog(self):
        return self.dogs.pop()

    def dequeueCat(self):
        return self.cats.pop()

    def getShelter(self):
        return self.total

    def getDogs(self):
        return self.dogs