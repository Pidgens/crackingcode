def b_search(arr, value, index=0):

    half = len(arr)/2

    midpoint = arr[half]
    # print 'MID: ', midpoint


    if midpoint == value:
        print 'ANSWER:',  index + half
    if midpoint < value:
        b_search(arr[half+1: len(arr)], value, index=half)
    if midpoint > value:
        index = half
        b_search(arr[0:half], value, index=index+half/2-1)

#############################################################
l1 = [3,4,5,6,7,8,9]

def b_search_iter(arr,  value):
    lower = 0
    upper = len(arr)
    while lower <= upper:
        mid = (lower + upper)/2
        if arr[mid] == value:
            return mid
        else:
            if value < arr[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
    return -1


def bs(array, value):
    first = 0
    last = len(array)-1
    found = False

    while not found and first <= last:
        mid = (first + last)//2
        if array[mid] == value:
            return True
        elif value > array[mid]:
            first = mid+1
        else:
            last = mid-1
    return found

print bs([1,2,3,4,5], 5)