__author__ = 'Derek Chiu'

# Insertion sort: Good for when data is nearly sorted (n). Else not good (n^2) runtime.
def insertion(z_list):
    for i in range(1, len(z_list)):
        curValue = z_list[i]
        position = i
        while (position>0) and z_list[position-1]>curValue:
            z_list[position] = z_list[position-1] # SWAP; peek at element before current
            position = position - 1
        z_list[position] = curValue

#Selection sort has a terrible run time and should only be used if the cost of swapping is high. O(n^2)
def selection(z_list):
    for i in range(len(z_list)-1, 0, -1): # Go from the last element to first element
        maxPos = 0
        for location in range(1, i+1):
            if z_list[location]>z_list[maxPos]:
                maxPos=location
        tmp = z_list[i]
        z_list[i] = z_list[maxPos]
        z_list[maxPos] = tmp

# Bubble Sort: Good for nearly sorted but takes 2 passes whereas insertion sort takes 1 pass.
# Total number of passes is (n-1); have (n-2) pairs
def bubble(z_list):
    for i in range(len(z_list)-1, 0, -1):
        for location in range(i):
            if z_list[location] > z_list[location+1]:
                tmp = z_list[location]
                z_list[location] = z_list[location+1]
                z_list[location + 1] = tmp

# Shell sort: Worse case depends on the increment sequence but when nearly sorted O(n log n)
# Normally is O(n^1.5). Based on insertion sort.
def shell(z_list):
    sublistCount=len(z_list)/2
    while (sublistCount > 0):
        for start_i in range(sublistCount):
            gapInsertionSort(z_list, start_i, sublistCount)
        sublistCount = sublistCount / 2

def gapInsertionSort(z_list, start, gap):
    for i in range(start+gap, len(z_list), gap):
        currentValue = z_list[i]
        pos = i
        while pos >= gap and z_list[pos-gap] > currentValue:
            z_list[pos] = z_list[pos - gap]
            pos = pos - gap
        z_list[pos] = currentValue

def mergeSort(z_list):
    if len(z_list) > 1:
        mid = len(z_list)/2
        leftHalf = z_list[:mid]
        rightHalf = z_list[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        # k - index of z_list
        # i - index of left
        # j - index of right
        i,j,k=0,0,0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                z_list[k] = leftHalf[i]
                i+= 1
            else:
                z_list[k] = rightHalf[j]
                j+=1
            k+=1

        while i < len(leftHalf):
            z_list[k] = leftHalf[i]
            i+= 1
            k+= 1

        while j < len(rightHalf):
            z_list[k] = rightHalf[j]
            j+= 1
            k+= 1
    return z_list

print 'MERGESORT', mergeSort([3,5,4,2,1])

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while left <= right and myList[right] >= pivot:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def qs(myList):
    return quicksort(myList, 0, len(myList)- 1)

a = [3,5,4,2,1]
print 'QUICKSORT', qs(a)

def heapSort(z_lst):
    length = len(z_lst)
    leastParent = length/2
    for i in range(leastParent, -1, -1):
        heapify(list, i, length)
    for i in range(length, 0 , -1):
        swap( list, 0, i)
        heapify(list, 0, i-1)

def heapify(z_lst, first, last):
    largest = 2 * first + 1
    if largest < last and z_lst[largest] < z_lst[largest+1]:
        swap( z_lst, largest, first)
        first = largest
        largest = 2 * first + 1
    else:
        return

def swap(list, x, y):
    tmp = list[x]
    list[x] = list[y]
    list[y] = tmp