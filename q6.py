
# FIB with caching...DP problem
def fib(i):
    cache = {}
    return fibHelper(i, cache)

def fibHelper(i, cache):
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i in cache.keys():
        return cache[i]
    cache[i] = fibHelper(i-1, cache) + fibHelper(i-2, cache)
    print 'CACHE', cache
    return cache[i]

# print 'ANSWER:', fib(5)

def stairsWay(num, cache):
    if num < 0:
        return 0
    elif num == 0:
        return 1
    elif cache[num] > -1:
        return cache[num]
    else:
        cache[num] = stairsWay(num - 1, cache) + stairsWay(num - 2, cache) + stairsWay(num - 3, cache)

    return cache[num]

def isFree(x ,y, limit=[(3,1)]):
    if x < 0 or y < 0 or (x,y) in limit:
        return False
    return True

def getPath(x, y, path, cache):
    point = (x,y)
    if point in cache.keys():
        return cache[point]
    print 'X:', x
    if x==0 and y==0:
        return True
    success = False
    if (x >= 1 and isFree(x-1,y)):
        success = getPath(x - 1, y, path, cache)
    if ( ( not success) and (y >= 1) and isFree(x,y-1) ):
        success = getPath(x, y-1, path, cache)
    if success:
        path.append(point)
    cache[point] = success
    print 'CACHE', cache
    return success

def bn_s(array, start, end):
    if end < start or start < 0 or end >= len(array):
        return False
    mid = (start + end)/2
    if mid == array[mid]:
        return mid
    elif mid < array[mid]:
        return bn_s(array, start, mid-1)
    else:
        return bn_s(array, mid+1, end)


def findMagicIndex(arr):
    return bn_s(arr, 0, len(arr)-1)

def getSubsets(big_set, index):
    if len(big_set) == index:
        allsubsets = []
        allsubsets.append([])
    else:
        allsubsets = getSubsets(big_set, index+1)
        item = big_set[index]
        moresubsets = []
        for array in allsubsets:
            newsubset = []
            newsubset += array
            newsubset.append(item)
            moresubsets.append(newsubset)
        allsubsets += moresubsets
    return allsubsets

def permutations(string, step = 0, path =[]):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        path.append(string)

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)

    return path

def per(s):
   if len(s) == 1:
     return [s]

   perm_list = [] # resulting list
   for a in s:
        # remaining_elements = []
        # for x in s:
        #     if x!=a:
        #         remaining_elements.append(x)
        remaining_elements = [x for x in s if x != a]
        # print 'RM', remaining_elements
        z = per(remaining_elements) # permutations of sublist

        for t in z:
            perm_list.append([a] + t)

   return perm_list


print per("ABC")