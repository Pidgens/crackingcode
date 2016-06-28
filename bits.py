__author__ = 'derekchiu'

import math
import decimal

def insertBits(n, m, i, j):

    ones = ~0
    left = ones << (j+1)
    right = (1 << i) - 1
    mask = left | right
    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted

# Given a positive integer, print the next smallest and the next largest number
# that have the same number of 1 bits in their binary representation

def getPrev(number):
    temp = number
    c0 = 0
    c1 = 0
    while (temp & 1) == 1:
        c1 += 1
        temp >>= 1
    if temp == 0:
        return -1
    while (temp & 1) == 0 and temp != 0:
        c0+=1
        temp>>=1
    p = c0 + c1
    number &= ((~0) << (p+1))
    mask = (1 << (c1 + 1))-1
    number |= mask << (c0 - 1)
    return number

def getNext(number):
    temp = number
    c0 = 0
    c1 = 0
    while (temp & 1) == 0 and  temp != 0:
        c0 += 1
        temp >>= 1
    while (temp & 1) == 1:
        c1 += 1
        temp >>= 1
    p = c0 + c1
    number |= 1 << p
    number &= ((~0) << (p))
    mask = (1 << (c1 - 1)) - 1
    number |= mask
    return number

def requiredBits(x, y):
    calc = x ^ y
    count = 0
    while calc != 0:
        if (calc & 1) == 1:
            count += 1
        calc >>= 1
    return count

def prime(num):
    if (num<2):
        return False
    sqrt = num**.5
    i = 2
    while i <= sqrt:
        if (num % i) == 0:
            return False
        i += 1
    return True

