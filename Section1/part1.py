import time
import random
import sys

total1 = 0
total2 = 0
print("Size\tInsertion\tMerge Sort")


def merge(A, p, q, r):
    """
    :param A: Array
    :param p: start of array
    :param q: middle of array
    :param r: end of array
    :return: Splits arrays
    """
    n1 = q - p + 1
    n2 = r - q
    # Let L[1...n1 + 1] and R[1...n2 + 1] be new arrays
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(0, n1):
        L[i] = A[p+i-1]
    for j in range(0, n2):
        R[j] = A[q+j]
    L[n1] = sys.maxsize
    R[n2] = sys.maxsize
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def merge_Sort(A, p, r):
    """
    :param A: Array
    :param p: start point
    :param r: end point
    :return: An array that is sorted
    """
    if p < r:
        q = (p+r)//2
        merge_Sort(A, p, q)
        merge_Sort(A, q + 1, r)
        merge(A, p, q, r)


for i in range(100, 10000, 250):
    randomList = random.sample(range(1, 10000), i)
    randomList2 = randomList
    k = i

    # Testing both Insertion and Merge sort
    # Insertion Sort
    start_time = time.perf_counter()
    for j in range(1, len(randomList)):
        key = randomList[j]
        i = j - 1
        while i >= 0 and randomList[i] > key:
            randomList[i+1] = randomList[i]
            i = i - 1
        randomList[i+1] = key

    end_time = time.perf_counter()
    start_time2 = time.perf_counter()

    merge_Sort(randomList2, 0, len(randomList2))

    end_time2 = time.perf_counter()
    total1 = end_time-start_time
    total2 = end_time2-start_time2

    print(k, "\t", total1, "\t", total2)
