#############################
import ll


#############################
#testing variables
q1test = False
q2test = False
q3test = False
q4test = False
q5test = False
q6test = False
q7test = False
q8test = False
q9test = False
q10test = True

#############################
# Determine if string has unique characters.
def uniqueString(s):
    hashtable = {}
    for char in s:
        if not char in hashtable:
            hashtable[char] = 1
            continue
        if hashtable[char] == 1:
            return False
        hashtable[char] = 1
    return True

if q1test:
    uniqueString('doggod')
    uniqueString('dog')
    uniqueString('doged')


#############################
# Reverse a string
def reverseString(s):
    index = len(s) - 1
    output_string = ''
    for _ in s:
        output_string += s[index]
        index -= 1
    return output_string

if q2test:
    reverseString('DOG')
    reverseString('HERO')

#############################
# Check if two strings are permutations of each other
def ifPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    hashtable = {}
    for char in s1:
        if not char in hashtable:
            hashtable[char] = 1
        else:
            hashtable+=1
    for char in s2:
        if char not in hashtable:
            return False
        if hashtable[char] == 0:
            return False
        else:
            hashtable[char] -= 1
    return True

if q3test:
    print ifPermutation('dog', 'godd')

#############################
def reverseWordsInString(s):
    listString = s.split(" ")
    index = len(listString) - 1
    output = ''
    for _ in listString:
        output += reverseString(listString[index]) + ' '
        index -= 1
    return output

if q4test:
    print reverseWordsInString("i ekil siht margorp yrev hcum")
    print reverseWordsInString("dog looc")

#######################################################################################
def removeDuplicatesLinkedList(head_node):
    hashtable = {}
    while head_node != None:
        data = head_node.getData()
        if data in hashtable:
            prev.setNext(head_node.getNext())
        else:
            prev = head_node
        head_node = head_node.getNext()
        hashtable[data] = 1

if q5test:
    linked_list = ll.LinkedList()
    linked_list.insert(3)
    linked_list.insert(3)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    removeDuplicatesLinkedList(linked_list.head)
    print 'NEW', linked_list.size()
    print linked_list.head.getData()
    print linked_list.head.getNext().getData()
    print linked_list.head.getNext().getNext().getData()

def findKthElementFromLast(linked_list, n):
    p1 = linked_list.head
    p2 = linked_list.head
    i2 = 0
    while i2 < (n-1):
        p2 = p2.getNext()
        i2 += 1
    while p2.getNext() != None:
        p2 = p2.getNext()
        p1 = p1.getNext()
    return p1.getData()

if q6test:
    linked_list = ll.LinkedList()
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.insert(6)
    linked_list.insert(7)
    print findKthElementFromLast(linked_list, 2)

def ifLinkedListCircular(head_node):
    p1 = head_node
    p2 = head_node
    first = True
    while p1 != p2 or first:
        first = False
        if p2.getNext() == None or p2.getNext().getNext() == None:
            return False
        p1 = head_node.getNext()
        p2 = head_node.getNext().getNext()
    return True

if q7test:
    linked_list2 = ll.LinkedList()
    linked_list2.insert(4)
    linked_list2.insert(5)
    linked_list2.insert(6)
    print 'LIST 2:', ifLinkedListCircular(linked_list2.head)

def reverseLinkedList(linked_list):
    rev = None
    current = linked_list.head
    while current != None:
        nextToSet = current.getNext()
        current.setNext(rev)
        rev = current
        current = nextToSet
    linked_list.head = rev

if q8test:
    linked_list = ll.LinkedList()
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    print 'BEFORE', linked_list.head.getData()
    reverseLinkedList(linked_list)
    print 'AFTER', linked_list.head.getData()

#######################################################################################
############################# STACKS ##################################################
#######################################################################################

class StackMinMax:
    def __init__(self):
        self.elems = []
        self.max = None
        self.min = None
    def peek(self):
        return self.elems[len(self.elems) - 1]
    def push(self, elem):
        if elem > self.max or self.max == None:
            self.max = elem
        if elem < self.min or self.min == None:
            self.min = elem
        return self.elems.append(elem)
    def pop(self):
        return self.elems.pop()
    def size(self):
        return len(self.elems)

if q9test:
    newStack = StackMinMax()
    newStack.push(3)
    newStack.push(4)
    print 'MIN:', newStack.min
    print 'MAX:', newStack.max

#######################################################################################
class QueueWithTwoStacks:
    def __init__(self):
        self.inbox = []
        self.outbox= []
    def enqueue(self, elem):
        self.inbox.append(elem)
    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

if q10test:
    q = QueueWithTwoStacks()
    q.enqueue(3)
    q.enqueue(4)
