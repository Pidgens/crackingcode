### You are given two sorted arrays, A and B, where A has a large enough buffer at the
### end to hold B. Write a method to merge B into A in sorted order.

def sortedArrays(A, B):
    i = 0
    j = 0
    origA =A[len(A)-1]
    origB =B[len(B)-1]

    while A[i] != origA or A[i] != origB:
        if A[i] > B[j]:
            A.insert( i, B[j])
            j+=1
            if j >= len(B):
                return A
        else:
            i+=1
    return A

A=[2,6,8,10]
B=[1,3,4,7]
print sortedArrays(A,B)
