__author__ = 'derekchiu'

import math
import decimal

def updateBit(num, i, value):
    mask = ~(1 << i)
    return (mask & num) | (value << i)

# number one
def insertBits(n, m, posi, posj):
    newM = (m << posi)
    return newM | n

# number two
def fractiontoBinary(number):
    first = int(number)
    start = float(.5)
    go = True
    secondPart = ''
    firstPart = bin(first) # in string form
    second = number - int(number)
    while go:

        if (second - start) >= 0:
            secondPart += '1'
            second = second - start
            if (second == 0):
                go = False
        else:
            secondPart += '0'
        start = start/float(2)

    x = firstPart + '.' + secondPart
    return x





def testBits():
    #########################################################################################################
    assert insertBits(1024, 19, 2, 6) == 1100, \
        "Got %d" % insertBits(1024, 19, 2, 6)
    assert insertBits(9, 3, 1, 2) == 15, "Got %d" % insertBits(9, 3, 1, 2)
    print "PASSED PROBLEM 1"
    #########################################################################################################
    assert fractiontoBinary(10.5) == "0b1010.1", "GOT %s" % fractiontoBinary(10.5)
    assert fractiontoBinary(10.75) == "0b1010.11", "GOT %s" % fractiontoBinary(10.75)
    assert fractiontoBinary(10.625) == "0b1010.101", "GOT %s" % fractiontoBinary(10.625)
    print "PASSED PROBLEM 2"
    #########################################################################################################

    print "PASSED PROBLEM 3"
    #########################################################################################################



testBits()
