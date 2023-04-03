# mergesort.py CODE -
import math
import numpy as np
import time
import sys


def merge(Arr, p, q, r, leftArr, rightArr) -> object:
    n1 = q - p
    n2 = r - q
    left = []
    right = []
    for i in range(0, n1):
        left.append(leftArr[i])

    for j in range(0, n2):
        right.append(rightArr[j])
    a = 0
    b = 0
    for k in range(p, r):  # iterate from 0 to 2
        if a >= len(left): # for the elements left in the array when other array is empty
            Arr[k] = right[b]
            b += 1
        elif b >= len(right): # for the elements left in the array when other array is empty
            Arr[k] = left[a]
            a += 1
        elif left[a] <= right[b]: # sorting the array
            Arr[k] = left[a]
            a = a + 1
        elif left[a] > right[b]: # sorting the array
            Arr[k] = right[b]
            b = b + 1
    return Arr


def mergeSort(Arr1: object) -> object:
    p = 0
    r = len(Arr1)
    i = 0
    if r > 1:
        if p < r:
            mid = math.ceil((p + r) / 2) # calculate mid of the array
            Arr1[p:mid] = mergeSort(Arr1[p: mid]) # divide with recursion
            Arr1[mid:r + 1] = mergeSort(Arr1[mid: r + 1]) # divide with recursion
            return merge(Arr1, p, mid, r, Arr1[p:mid], Arr1[mid:r + 1])
        else:
            return Arr1
        return Arr1
    return Arr1


def writeInTextFile20(A: object) -> object:
    file1 = open("arr20.txt", "w+") # Creates a file with the file name
    file1.write(str(np.array(A)))
    '''print("Output of Readline function is ")
    print(file1.read())'''
    file1.close()


def writeInTextFile100(A: object) -> object:
    file1 = open("arr100.txt", "w+") # Creates a file with the file name
    file1.write(str(np.array(A)))
    '''print("Output of Readline function is ")
    print(file1.read())'''
    file1.close()


def writeInTextFile1000(A: object) -> object:
    file1 = open("arr1000.txt", "w+") # Creates a file with the file name
    file1.write(str(np.array(A)))
    '''print("Output of Readline function is ")
    print(file1.read())'''
    file1.close()


def writeInTextFile4000(A: object) -> object:
    file1 = open("arr4000.txt", "w+") # Creates a file with the file name
    file1.write(str(np.array(A)))
    '''print("Output of Readline function is ")
    print(file1.read(len(A)))'''
    file1.close()

#driver code
if __name__ == "__main__":
    #  A = [89, 54, 14, 68, 23, 6, 44]
    np.set_printoptions(threshold=sys.maxsize)

    A = np.random.randint(1, 6000, 20)
    writeInTextFile20(A)
    print("Given 20 Array - ", A)
    startmilliseconds20 = int(time.time() * 1000)
    print("startmilliseconds20", startmilliseconds20)
    print("Sorted 20 Array - ", mergeSort(A)) # merge sort start
    endmilliseconds20 = int(time.time() * 1000)
    print("endmilliseconds20", endmilliseconds20)
    print("Total time to sort 20 elements", endmilliseconds20 - startmilliseconds20)
    print("--------------------------------------------------------------------------------------------")
    A = np.random.randint(1, 6000, 100)
    writeInTextFile100(A)
    print("Given 100 Array - ", A)
    startmilliseconds100 = int(time.time() * 1000)
    print("startmilliseconds100", startmilliseconds100)
    print("Sorted 100 Array - ", mergeSort(A)) # merge sort start
    endmilliseconds100 = int(time.time() * 1000)
    print("endmilliseconds100", endmilliseconds100)
    print("Total time to sort 100 elements", endmilliseconds100 - startmilliseconds100)
    print("--------------------------------------------------------------------------------------------")
    A = np.random.randint(1, 6000, 1000)
    writeInTextFile1000(A)
    print("Given 1000 Array - ", A)
    startmilliseconds1000 = int(time.time() * 1000)
    print("startmilliseconds", startmilliseconds1000)
    print("Sorted 1000 Array - ", mergeSort(A)) # merge sort start
    endmilliseconds1000 = int(time.time() * 1000)
    print("endmilliseconds1000", endmilliseconds1000)
    print("Total time to sort 1000 elements", endmilliseconds1000 - startmilliseconds1000)
    print("--------------------------------------------------------------------------------------------")
    A = np.random.randint(1, 6000, 4000)
    writeInTextFile4000(A)
    print("Given 4000 Array - ", str(A))
    startmilliseconds4000 = int(time.time() * 1000)
    print("startmilliseconds", startmilliseconds4000)
    print("Sorted 4000 Array - ", mergeSort(A)) # merge sort start
    endmilliseconds4000 = int(time.time() * 1000)
    print("endmilliseconds4000", endmilliseconds4000)
    print("Total time to sort 4000 elements", endmilliseconds4000 - startmilliseconds4000)
    print("--------------------------------------------------------------------------------------------")
    print("Total time to sort 20 elements", endmilliseconds20 - startmilliseconds20)
    print("Total time to sort 100 elements", endmilliseconds100 - startmilliseconds100)
    print("Total time to sort 1000 elements", endmilliseconds1000 - startmilliseconds1000)
    print("Total time to sort 4000 elements", endmilliseconds4000 - startmilliseconds4000)
