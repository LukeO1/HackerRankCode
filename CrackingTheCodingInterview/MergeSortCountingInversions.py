#!/bin/python3

"""Count the number of inversions (swaps when A[i] > B[j]) while doing merge sort."""
import sys

#Use global variable to count number of inversions
count = 0

def countInversions(arr):
    global count
    split(arr)
    return count

def split(arr):
    #If arr has more than one element, then split
    if len(arr) > 1:
        mid = len(arr)//2
        #print("mid:", mid)
        #print("arr", arr)
        A = split(arr[0:mid])
        B = split(arr[mid:])
    #Else return the arr
    else:
        return arr
    #Pass A and B to be merged
    return merge(A, B)

def merge(A, B):
    global count
    #print("A", A)
    #print("B", B)
    #Initiate pointers to iterate over A and B, and create a new array C where the merged element will go
    i = 0
    j = 0
    C = []
    #While pointers not at the end of either A and B compare and merge into new array C
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
            # Add up inversions by summing up the remainder elements left in A
            count += (len(A) - i)

    #If there are still elements in A, add them to C
    while i < len(A):
        C.append(A[i])
        i += 1

    #If there are still elements in B, add them to C
    while j < len(B):
        C.append(B[j])
        j += 1
    return C

#Function from hackerrank, can substitute for anything else
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)

