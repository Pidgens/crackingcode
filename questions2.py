###############################################################
################### HEAP QUESTIONS ############################
###############################################################
def leftChildOfHeap(heap, index):
    return (2*index)+1

def rightChildOfHeap(heap, index):
    return (2*index)+2

def parentAtNode(heap, index):
    return (index-1)/2

###############################################################

class BinaryHeap:
    def __init__(self):
        self.heapList = []
        self.size = 0

    def percolateUp(self, i):
        parentNode = (i - 1) // 2
        while parentNode > 0:
            if self.heapList[i] < self.heapList[parentNode]:
                tmp = self.heapList[parentNode]
                self.heapList[parentNode] = self.heapList[i]
                self.heapList[i] = tmp
            parentNode = parentAtNode(self.heapList, parentNode)

    def insert(self, k):
        self.heapList.append(k)
        self.size += 1
        self.percolateUp(self.size)

    def percolateDown(self, i ):
        while ( i * 2 ) <= self.size:
            minChild = self.minChild(i)
            if self.heapList(i) > self.heapList(minChild):
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minChild]
                self.heapList[minChild] = tmp
            i = minChild

    def minChild(self, i):
        if (i * 2) + 1  > self.size:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def deleteMin(self):
        retval = self.heapList[0]
        self.heapList[0] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.percolateDown(0)
        return retval