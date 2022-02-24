# mergeSort.py CODE -
import math


def merge(Arr, p, q, r, leftArr, rightArr ) -> object:
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
        if a >= len(left):
            Arr[k] = right[b]
            b += 1
        elif b >= len(right):
            Arr[k] = left[a]
            a += 1
        elif left[a] <= right[b]:
            Arr[k] = left[a]
            a = a + 1
        elif left[a] > right[b]:
            Arr[k] = right[b]
            b = b + 1
    return Arr


def mergeSort(Arr1: object) -> object:
    p = 0
    r = len(Arr1)
    i = 0
    if r > 1:
        if p < r:
            mid = math.ceil((p + r) / 2)
            Arr1[p:mid] = mergeSort(Arr1[p: mid])
            Arr1[mid:r+1] = mergeSort(Arr1[mid: r + 1])
            return merge(Arr1, p, mid, r, Arr1[p:mid], Arr1[mid:r + 1])
        else:
            return Arr1
        return Arr1
    return Arr1



if __name__ == "__main__":
    A = [89, 54, 14, 68, 23, 6, 44]
    print("Given Array - ", A)
    print("Sorted Array - ", mergeSort(A))
