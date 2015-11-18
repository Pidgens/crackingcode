__author__ = 'derekchiu'

# def staircase():
#     n = int(input())
#     output = ''
#     for i in range(n):
#         output += ((n-i) * ' ')
#         output += ( ((i+1) * '#'))
#         if (n > (i+1)):
#             output += '\n'
#     print(output)
#
# staircase()

import re
def differencePairs(inputString):

    lines = []
    for line in re.split('\n', inputString):
        lines.append(line.split(' '))

    # Split different fields
    numberofInts = int(lines[0][0])
    differenceGoal = int(lines[0][0])
    count = 0

    # NOT EFFICIENT. BETTER WAY?
    for n in lines[1]:

        for second_pass in lines[1]:
            print n
            if (int(n) - int(second_pass) == differenceGoal):
                count += 1
    print count
    return count

differencePairs("5 2 \n1 5 3 4 2")
