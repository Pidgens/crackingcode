def calcCoins(n, highest_coin):
    nextDenom = 0

    if highest_coin == 25:
        nextDenom = 10
    elif highest_coin == 10:
        nextDenom = 5
    elif highest_coin == 5:
        nextDenom = 1
    elif highest_coin == 1:
        return 1
    ways = 0
    i = 0
    while (i*highest_coin <= n):
        ways += calcCoins(n-i*highest_coin, nextDenom)
        i+=1
        print 'I', highest_coin
        print 'WAYS', ways
    return ways

def permutations(s1):
    if len(s1) == 1:
        return [s1]
    perm = []
    for c1 in s1:
        remain = [x for x in s1 if x != c1]
        new = permutations(remain)
        print 'NEW', new
        for item in new:
            perm.append([c1] + item)
            # print 'perm', perm
    return perm

def gcd(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)

def pascalsTriangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        newRow = [1]
        result = pascalsTriangle(n-1)
        prevRow = result[-1]
        for i in range(len(prevRow)-1):
            newRow.append(prevRow[i] + prevRow[i+1])
        newRow += [1]
        result.append(newRow)
    return result

print pascalsTriangle(3)