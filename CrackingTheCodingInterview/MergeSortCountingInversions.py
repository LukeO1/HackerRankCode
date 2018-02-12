#!/bin/python3

import sys
count = 0

def countInversions(arr):
    global count
    split(arr)
    return count

def split(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        #print("mid:", mid)
        #print("arr", arr)
        A = split(arr[0:mid])
        B = split(arr[mid:])
    else:
        return arr
    return merge(A, B)

def merge(A, B):
    global count
    #print("A", A)
    #print("B", B)
    i = 0
    j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            #print("A is:", A[i], "and B is:", B[j])
            j += 1
            #print("here")
            count += (len(A) - i)

    while i < len(A):
        C.append(A[i])
        i += 1

    while j < len(B):
        C.append(B[j])
        j += 1
    return C

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)

