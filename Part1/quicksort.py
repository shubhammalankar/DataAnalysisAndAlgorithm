import numpy as np
import sys
import time


def partition(Arr, low, high) -> object:
    i = (low - 1)
    pivot = Arr[high] # considered the last element
    for j in range(low, high):
        if Arr[j] <= pivot:
            i = i + 1
            Arr[i], Arr[j] = Arr[j], Arr[i]
    Arr[i + 1], Arr[high] = Arr[high], Arr[i + 1] # shifting it to the mid to get a sorted array
    return i + 1


def quickSort(A, low, high) -> object:
    if len(A) == 1:
        return A
    if low < high:
        pi = partition(A, low, high)
        quickSort(A, low, pi - 1)
        quickSort(A, pi + 1, high)
    return A


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
    # A = [10, 7, 8, 9, 1, 5]
    np.set_printoptions(threshold=sys.maxsize)

    A = np.random.randint(1, 6000, 20)
    writeInTextFile20(A)
    print("Sorted array -", A)
    startmilliseconds20 = int(time.time() * 1000)
    print("startmilliseconds20", startmilliseconds20)
    print("Sorted array -", quickSort(A, 0, len(A) - 1))
    endmilliseconds20 = int(time.time() * 1000)
    print("endmilliseconds20", endmilliseconds20)
    print("Total time to sort 20 elements", endmilliseconds20 - startmilliseconds20)
    print("--------------------------------------------------------------------------------------------")
    A = np.random.randint(1, 6000, 100)
    writeInTextFile100(A)
    print("Sorted array -", A)
    startmilliseconds100 = int(time.time() * 1000)
    print("startmilliseconds100", startmilliseconds100)
    print("Sorted array -", quickSort(A, 0, len(A) - 1))
    endmilliseconds100 = int(time.time() * 1000)
    print("endmilliseconds100", endmilliseconds100)
    print("Total time to sort 100 elements", endmilliseconds100 - startmilliseconds100)
    print("--------------------------------------------------------------------------------------------")
    A = np.random.randint(1, 6000, 1000)
    writeInTextFile1000(A)
    print("Sorted array -", A)
    startmilliseconds1000 = int(time.time() * 1000)
    print("startmilliseconds", startmilliseconds1000)
    print("Sorted array -", quickSort(A, 0, len(A) - 1))
    endmilliseconds1000 = int(time.time() * 1000)
    print("endmilliseconds1000", endmilliseconds1000)
    print("Total time to sort 1000 elements", endmilliseconds1000 - startmilliseconds1000)
    print("--------------------------------------------------------------------------------------------")
    A = np.random.randint(1, 6000, 4000)
    writeInTextFile4000(A)
    print("Sorted array -", A)
    startmilliseconds4000 = int(time.time() * 1000)
    print("startmilliseconds", startmilliseconds4000)
    print("Sorted array -", quickSort(A, 0, len(A) - 1))
    endmilliseconds4000 = int(time.time() * 1000)
    print("endmilliseconds4000", endmilliseconds4000)
    print("Total time to sort 4000 elements", endmilliseconds4000 - startmilliseconds4000)
    print("--------------------------------------------------------------------------------------------")
    print("Total time to sort 20 elements", endmilliseconds20 - startmilliseconds20)
    print("Total time to sort 100 elements", endmilliseconds100 - startmilliseconds100)
    print("Total time to sort 1000 elements", endmilliseconds1000 - startmilliseconds1000)
    print("Total time to sort 4000 elements", endmilliseconds4000 - startmilliseconds4000)
