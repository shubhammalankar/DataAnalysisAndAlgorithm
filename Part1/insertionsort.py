# mergeSort.py CODE -
import numpy as np
import sys
import time


def insertionSort(Arr: object) -> object:
    for j in range(1, len(Arr)):
        key = Arr[j]
        i = j - 1
        while i >= 0 and key < Arr[i]:
            Arr[i + 1] = Arr[i] # swap
            i = i - 1
        A[i + 1] = key # swap
    return Arr


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
    # A = [89, 54, 14, 68, 23, 6, 44]
    # A = np.random.randint(1, 6000, 20)
    np.set_printoptions(threshold=sys.maxsize)

    A = np.random.randint(1, 6000, 20)
    writeInTextFile20(A)
    print("Given 20 Array - ", A)
    startmilliseconds20 = int(time.time() * 1000)
    print("startmilliseconds20", startmilliseconds20)
    print("Sorted 20 Array - ", insertionSort(A))
    endmilliseconds20 = int(time.time() * 1000)
    print("endmilliseconds20", endmilliseconds20)
    print("Total time to sort 20 elements", endmilliseconds20 - startmilliseconds20)
    print("--------------------------------------------------------------------------------------------")
    A = np.random.randint(1, 6000, 100)
    writeInTextFile100(A)
    print("Given 100 Array - ", A)
    startmilliseconds100 = int(time.time() * 1000)
    print("startmilliseconds100", startmilliseconds100)
    print("Sorted 100 Array - ", insertionSort(A))
    endmilliseconds100 = int(time.time() * 1000)
    print("endmilliseconds100", endmilliseconds100)
    print("Total time to sort 100 elements", endmilliseconds100 - startmilliseconds100)
    print("--------------------------------------------------------------------------------------------")
    A = np.random.randint(1, 6000, 1000)
    writeInTextFile1000(A)
    print("Given 1000 Array - ", A)
    startmilliseconds1000 = int(time.time() * 1000)
    print("startmilliseconds", startmilliseconds1000)
    print("Sorted 1000 Array - ", insertionSort(A))
    endmilliseconds1000 = int(time.time() * 1000)
    print("endmilliseconds1000", endmilliseconds1000)
    print("Total time to sort 1000 elements", endmilliseconds1000 - startmilliseconds1000)
    print("--------------------------------------------------------------------------------------------")
    A = np.random.randint(1, 6000, 4000)
    writeInTextFile4000(A)
    print("Given 4000 Array - ", str(A))
    startmilliseconds4000 = int(time.time() * 1000)
    print("startmilliseconds", startmilliseconds4000)
    print("Sorted 4000 Array - ", insertionSort(A))
    endmilliseconds4000 = int(time.time() * 1000)
    print("endmilliseconds4000", endmilliseconds4000)
    print("Total time to sort 4000 elements", endmilliseconds4000 - startmilliseconds4000)
    print("--------------------------------------------------------------------------------------------")
    print("Total time to sort 20 elements", endmilliseconds20 - startmilliseconds20)
    print("Total time to sort 100 elements", endmilliseconds100 - startmilliseconds100)
    print("Total time to sort 1000 elements", endmilliseconds1000 - startmilliseconds1000)
    print("Total time to sort 4000 elements", endmilliseconds4000 - startmilliseconds4000)