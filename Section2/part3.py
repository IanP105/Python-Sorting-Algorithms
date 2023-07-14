import math
import time
from random import randint
from itertools import permutations


def quicksort(A, p, r):
    """
    Quicksort algorithm where index 'r' is the pivot.
    :param A: (List) of ints to sort
    :param p: (int) smallest index of A
    :param r: (int) largest index of A
    :return:  (None)
    """
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    """
    Partitioning function of quicksort.
    :param A: (list) of ints to partition
    :param p: (int) lower partitioning bounds
    :param r: (int) uppoer partitioning bounds and pivot index
    :return: (int) index of the pivot's new location in A
    """
    x = A[r]

    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]  # swap A[i] and A[j]
    A[i + 1], A[r] = A[r], A[i + 1]  # swap A[i+1] and A[r]
    return i + 1


def randomized_quicksort(A, p, r):
    """
    Quicksort algorithm where a random index is the pivot.
    :param A: (List) of ints to sort
    :param p: (int) smallest index of A
    :param r: (int) largest index of A
    :return:  (None)
    """
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)


def randomized_partition(A, p, r):
    """
    Pick a random partitioning index and swap with index 'r' in A
    before partitioning.
    """
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]

    return partition(A, p, r)


def mo3_quicksort(A, p, r):
    """
    Quicksort using the median-of-3.
    :param A: (List) of ints to sort
    :param p: (int) smallest index of A
    :param r: (int) largest index of A
    :return:  (None)
    """
    if p < r:
        q = mo3_partition(A, p, r)
        mo3_quicksort(A, p, q - 1)
        mo3_quicksort(A, q + 1, r)


def mo3_partition(A, p, r):
    """
    Pick the medion of 3 values of indexes p, r, adn p + r DIV 2 and
    swap with index 'r' in A before partitioning.
    """
    i = r
    if r - p > 1:  # Only use mo3 when A has more than 2 elements
        q = (p + r) // 2  # middle index of A
        if A[p] <= A[q] <= A[r] or A[r] <= A[q] <= A[p]:
            i = q
        elif A[q] <= A[p] <= A[r] or A[r] <= A[p] <= A[q]:
            i = p
        # else A[r] is the median
        A[r], A[i] = A[i], A[r]

    return partition(A, p, r)


def heapsort(A):
    """
    Algorithm for heapsort.
    :param A: (list) of ints to sort.
    :return: (None)
    """
    build_max_heap(A)
    for i in range(len(A) - 1, 1, -1):
        A[1], A[i] = A[i], A[1]
        A[0] = A[0] - 1
        max_heapify(A, 1)


def left(i):
    """
    The left child-node of the element at index i in the heap.
    """
    return i * 2


def right(i):
    """
    The right child-node of the element at index i in the heap.
    """
    return i * 2 + 1


def build_max_heap(A):
    """
    Subfunction for building a max heap in heap.
    """
    A[0] = len(A) - 1
    for i in range(A[0] // 2, 0, -1):
        max_heapify(A, i)


def max_heapify(A, i):
    """
    Subfunction that reorders the element into a max heap.
    """
    l = left(i)
    r = right(i)
    largest = l if l <= A[0] and A[l] > A[i] else i
    if r <= A[0] and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def mergesort(A, p, r):
    """
    Algorithm for mergesort.
    :param A: (List) of ints to sort
    :param p: (int) smallest index of A
    :param r: (int) largest index of A
    :return: (None)
    """
    if p < r:
        q = (p + r) // 2
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    """
    Merge function of mergesort.
    """
    n_1 = q - p + 1
    n_2 = r - q
    L = [A[p + x] for x in range(n_1)]
    R = [A[q + 1 + x] for x in range(n_2)]
    L.append(math.inf)
    R.append(math.inf)

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def test():
    """
    Test function for quicksort implementation.
    :return: None
    """
    def perm_test(int_list):
        for perm in permutations(int_list):
            test_list = list(perm)
            mergesort(test_list, 0, len(test_list) - 1)
            assert test_list == sorted(test_list), \
                f"Mergesort: {list(perm)} should be {sorted(test_list)} but got {test_list}"

            test_list = list(perm)
            quicksort(test_list, 0, len(test_list) - 1)
            assert test_list == sorted(test_list), \
                f"Quicksort: {list(perm)} should be {sorted(test_list)} but got {test_list}"

            test_list = list(perm)
            mo3_quicksort(test_list, 0, len(test_list) - 1)
            assert test_list == sorted(test_list), \
                f"MO3 Quicksort: {list(perm)} should be {sorted(test_list)} but got {test_list}"

            test_list = list(perm)
            randomized_quicksort(test_list, 0, len(test_list) - 1)
            assert test_list == sorted(test_list), \
                f"Randomized Quicksort: {list(perm)} should be {sorted(test_list)} but got {test_list}"

            test_list = list(perm)
            heap_test_list = [None] + test_list
            heapsort(heap_test_list)
            assert heap_test_list[1:] == sorted(test_list), \
                f"Heapsort: {list(perm)} should be {sorted(test_list)} but got {heap_test_list[1:]}"

        print(f"All tests passed for {int_list}")

    perm_test([])
    perm_test([1])
    perm_test([0, 1])
    perm_test([1, 1])
    perm_test([1, 2, 3])
    perm_test([2, 2, 5, 5])
    perm_test([-2, 4, 6, 8])


def qsort_fail():
    print('n items' '\t', 'time (s)')
    for i in range(1, 1000):
        arr = sorted([randint(-1000, 1001) for _ in range(i)])
        n = len(arr)

        t_start = time.perf_counter()
        quicksort(arr, 0, n-1)
        t_delta = time.perf_counter() - t_start
        print(n, '\t', t_delta)


def qsort_compare():
    print('n items', '\t', 'quicksort', '\t', 'random-quicksort', '\t', 'mergesort', '\t', 'heapsort')
    for i in range(50, 1000, 50):
        arr = sorted([randint(-1000, 1001) for _ in range(i)])
        n = len(arr)

        t_start = time.perf_counter()
        quicksort(arr, 0, n - 1)
        qsort = time.perf_counter() - t_start

        t_start = time.perf_counter()
        randomized_quicksort(arr, 0, n - 1)
        r_qsort = time.perf_counter() - t_start

        t_start = time.perf_counter()
        mergesort(arr, 0, n - 1)
        msort = time.perf_counter() - t_start

        t_start = time.perf_counter()
        heapsort(arr)
        hsort = time.perf_counter() - t_start

        print(n, '\t', qsort, '\t', r_qsort, '\t', msort, '\t', hsort)


def random_qsort_compare(start, stop, step):
    print('n items', '\t', 'random-quicksort', '\t', 'mergesort', '\t', 'heapsort')
    for i in range(start, stop, step):
        arr = sorted([randint(-1000, 1001) for _ in range(i)])
        n = len(arr)

        t_start = time.perf_counter()
        randomized_quicksort(arr, 0, n - 1)
        r_qsort = time.perf_counter() - t_start

        t_start = time.perf_counter()
        mergesort(arr, 0, n - 1)
        msort = time.perf_counter() - t_start

        t_start = time.perf_counter()
        heapsort(arr)
        hsort = time.perf_counter() - t_start

        print(n, '\t', r_qsort, '\t', msort, '\t', hsort)


if __name__ == '__main__':
    # test()
    # qsort_fail()
    qsort_compare()
    random_qsort_compare(1000, 100001, 1000)
