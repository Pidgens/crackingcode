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
            