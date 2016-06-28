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

print permutations("ABC")