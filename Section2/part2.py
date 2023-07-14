import random, time, sys
from itertools import permutations


print("Size\tMerge\tQuick\tHeap")

# Heap Sort
def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    largest = None
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)


def build_max_heap(A):
    heap_size = len(A)-1
    for i in range((len(A)-1) // 2, 0, -1):
        max_heapify(A, i, heap_size)
    return heap_size


def heap_sort(A):
    heap_size = build_max_heap(A)
    # print('max_heap:',A)
    for i in range(len(A)-1, 1, -1):
        A[1], A[i] = A[i], A[1]
        heap_size -= 1
        max_heapify(A, 1, heap_size)


def quickSort(A, p, r):
    """
    :param A: Array
    :param p: beginning of array
    :param r: end of array
    :return: Sorted array
    """
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)



def partition(A, p, r):
    """
    :param A: Array
    :param p: beginning of array being partitioned
    :param r: end of array being partitioned
    :return: Where to start sorting
    """
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


# Merge Sort
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
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    L[n1] = sys.maxsize
    R[n2] = sys.maxsize
    i = 0
    j = 0
    for k in range(p, r + 1):
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


# Random list maker
for i in range(100, 10000, 250):
    total1 = 0
    total2 = 0
    total3 = 0
    randomList = random.sample(range(1, 100000), i)
    randomList2 = randomList.copy()
    randomList3 = randomList.copy()
    randomList3.insert(0, None)

    # Merge sort timed
    start_time = time.perf_counter()

    merge_Sort(randomList, 0, len(randomList) - 1)

    end_time = time.perf_counter()


    # Quick sort timed
    start_time2 = time.perf_counter()

    quickSort(randomList2, 0, len(randomList2)-1)

    end_time2 = time.perf_counter()


    # Heap sort timed
    start_time3 = time.perf_counter()

    heap_sort(randomList3)

    end_time3 = time.perf_counter()

    merge_time = end_time - start_time
    quick_time = end_time2 - start_time2
    heap_time = end_time3 - start_time3


    print(i, "\t", merge_time, "\t", quick_time, "\t", heap_time)

# print(f"Quick sort: {randomList2}")
# print(f"Merge sort: {randomList}")
# print(f"Heap sort: {randomList3}")

#
# def heap_test(A):
#     correct = True
#     total_len = len(A)
#     while total_len > 1:
#         for i in range(1, len(A) - 1):
#             if A[i] <= A[i+1]:
#                 total_len -= 1
#             else:
#                 print("Index:", i, "Number:", A[i], "is not <=", A[i+1], "index:", i+1)
#                 correct = False
#                 total_len -= 1
#     return correct
#
# def sorted_test(A):
#     correct = True
#     total_len = len(A)
#     while total_len > 1:
#         for i in range(0, len(A) - 1):
#             if A[i] <= A[i+1]:
#                 total_len -= 1
#             else:
#                 print("Index:", i, "Number:", A[i], "is not <=", A[i+1], "index:", i+1)
#                 correct = False
#                 total_len -= 1
#     return correct
#
# print("-------------------------------------------")
# print("Heap sort works: ", heap_test(randomList3))
# print("-------------------------------------------")
# print("Merge sort works: ",sorted_test(randomList))
# print("-------------------------------------------")
# print("Quick sort works: ",sorted_test(randomList2))
# print("-------------------------------------------")






