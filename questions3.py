####################################################################
####################################################################
####################################################################

import ll

t1 = True
t2 = False
t3 = False


def deleteMiddleNodeLinkedList(middle_node):
    nextData = middle_node.getNext().getData()
    nextNext = middle_node.getNext.getNext()
    middle_node.setData(nextData)
    middle_node.setNext(nextNext)

if t1:
    linkedList = ll.LinkedList()
    linkedList.insert(1)
    linkedList.insert(2)
    linkedList.insert(3)
    linkedList.insert(4)
    linkedList.insert(5)
    print linkedList.head.getNext().getNext().getData()

def partitionLinkedListX(head_node , x):
    beforeStart = None
    afterStart = None
    while head_node != None:
        print 'head_node', head_node.getData()
        next = head_node.getNext()
        if head_node.getData() < x:
            head_node.setNext(beforeStart)
            beforeStart = head_node
        else:
            head_node.setNext(afterStart)
            afterStart = head_node
        head_node = next

    if beforeStart == None:
        return afterStart

    head = beforeStart
    while beforeStart.getNext() != None:
        beforeStart = beforeStart.getNext()
    beforeStart.setNext(afterStart)
    return head


if t2:
    linkedList = ll.LinkedList()
    linkedList.insert(5)
    linkedList.insert(4)
    linkedList.insert(2)
    linkedList.insert(1)
    linkedList.insert(3)
    # print linkedList.head.getData()
    linkedList = partitionLinkedListX(linkedList.head, 3)
    print '#:', linkedList.getData()
    print '1:', linkedList.getNext().getData()
    print '2:', linkedList.getNext().getNext().getData()
    print '3:', linkedList.getNext().getNext().getNext().getData()
    print '3:', linkedList.getNext().getNext().getNext().getNext().getData()

def addTwoLinkedList(l1, l2):
    l1Pointer = l1.head
    l2Pointer = l2.head
    sumLL = ll.LinkedList()
    currentCarry = 0
    nextCarry = 0
    if l1.size() > l2.size():
        # pad 0s
        while l2.size() < l1.size():
            l2.insert(0)
    if l1.size() < l2.size():
        while l2.size() > l1.size():
            l1.insert(0)
    while l1Pointer != None:
        cur_sum = l1Pointer.getData() + l2Pointer.getData()
        if cur_sum >= 10:
            cur_sum = cur_sum % 10
            nextCarry = 1
        else:
            nextCarry = 0

        sumLL.insert(carry + cur_sum)

        l1Pointer = l1Pointer.getNext()
        l2Pointer = l2Pointer.getNext()

    return sumLL

if t3:
    linkedList = ll.LinkedList()
    linkedList.insert(1)
    print 'HEAD1:', linkedList.head.getData()
    linkedList.insert(3)
    print 'HEAD2:', linkedList.head.getData()
    linkedList.insert(7)
    print 'HEAD3:', linkedList.head.getData()
    linkedList2 = ll.LinkedList()
    linkedList2.insert(5)
    linkedList2.insert(6)
    linkedList2.insert(4)
    sum_ll = addTwoLinkedList(linkedList, linkedList2)
    print sum_ll.head.getData()
    print sum_ll.head.getNext().getData()
    print sum_ll.head.getNext().getNext().getData()