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

print b_search_iter(l1, 5)