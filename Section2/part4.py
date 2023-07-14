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
    :param r: (int) upper partitioning bounds and pivot index
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
    Pick the median of 3 values of indexes p, r, adn p + r DIV 2 and
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


def test():
    """
    Test function for quicksort implementation.
    :return: None
    """
    def perm_test(int_list):
        for perm in permutations(int_list):
            test_list = list(perm)

            test_list = list(perm)
            quicksort(test_list, 0, len(test_list) - 1)
            assert test_list == sorted(test_list), \
                f"Quicksort: {list(perm)} should be {sorted(test_list)} but got {test_list}"

            test_list = list(perm)
            randomized_quicksort(test_list, 0, len(test_list) - 1)
            assert test_list == sorted(test_list), \
                f"Randomized Quicksort: {list(perm)} should be {sorted(test_list)} but got {test_list}"

            test_list = list(perm)
            mo3_quicksort(test_list, 0, len(test_list) - 1)
            assert test_list == sorted(test_list), \
                f"MO3 Quicksort: {list(perm)} should be {sorted(test_list)} but got {test_list}"

        print(f"All tests passed for {int_list}")

    perm_test([])
    perm_test([1])
    perm_test([0, 1])
    perm_test([1, 1])
    perm_test([1, 2, 3])
    perm_test([2, 2, 5, 5])
    perm_test([-2, 4, 6, 8])


def random_qsort_compare(start, stop, step):
    print('n items', '\t', 'quicksort', '\t', 'random-quicksort', '\t', 'mo3-quicksort')
    for i in range(start, stop, step):
        arr = [randint(-1000, 1001) for _ in range(i)]
        n = len(arr)

        t_start = time.perf_counter()
        quicksort(arr, 0, n - 1)
        qsort = time.perf_counter() - t_start

        t_start = time.perf_counter()
        randomized_quicksort(arr, 0, n - 1)
        r_qsort = time.perf_counter() - t_start

        t_start = time.perf_counter()
        mo3_quicksort(arr, 0, n - 1)
        m_qsort = time.perf_counter() - t_start

        print(n, '\t', qsort, '\t', r_qsort, '\t', m_qsort)


def sorted_qsort_compare(start, stop, step):
    print('n items', '\t', 'quicksort', '\t', 'random-quicksort', '\t', 'mo3-quicksort')
    for i in range(start, stop, step):
        arr = sorted([randint(-1000, 1001) for _ in range(i)])
        n = len(arr)

        t_start = time.perf_counter()
        quicksort(arr, 0, n - 1)
        qsort = time.perf_counter() - t_start

        t_start = time.perf_counter()
        randomized_quicksort(arr, 0, n - 1)
        r_qsort = time.perf_counter() - t_start

        t_start = time.perf_counter()
        mo3_quicksort(arr, 0, n - 1)
        m_qsort = time.perf_counter() - t_start

        print(n, '\t', qsort, '\t', r_qsort, '\t', m_qsort)


if __name__ == '__main__':
    random_qsort_compare(10, 1000, 10)
    sorted_qsort_compare(10, 1000, 10)
