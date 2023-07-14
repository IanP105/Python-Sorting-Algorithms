import time, random
from itertools import permutations

import numpy as np


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


# def test():
#     """
#     Test function for heapsort implementation.
#     :return: None
#     """
#     def perm_test(int_list):
#         for perm in permutations(int_list):
#             test_list = list(perm)
#             test_list.insert(0,None)
#             print(test_list)
#             heap_sort(test_list)
#             assert test_list[1:] == sorted(list(perm)), f"{list(perm)} should be {sorted(test_list)} but got {test_list}"
#             print(f"{list(perm)} --> {test_list[1:]}")
#
#     perm_test([])
#     perm_test([1])
#     perm_test([0, 1])
#     perm_test([1, 1])
#     perm_test([1, 2, 3])
#     perm_test([2, 2, 5, 5])
#     perm_test([-2, 4, 6, 8])

print("N\tTime Random\tTime Sorted")
for N in range(100, 10000, 250):
    A = [None]
    B = [e for e in range(N)]
    B.insert(0,None)
    for i in range(N):
        A.append(random.randint(-2*N, 2*N-1))
    # print(A)
    start_time_random = time.perf_counter()
    heap_sort(A)
    end_time_random = time.perf_counter()
    # print(A)
    # print(B)
    start_time_sorted = time.perf_counter()
    heap_sort(B)
    end_time_sorted = time.perf_counter()
    # print(B)
    print(N, '\t', end_time_random - start_time_random, '\t', end_time_sorted - start_time_sorted)
