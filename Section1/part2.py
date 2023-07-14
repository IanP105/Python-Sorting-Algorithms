import time
import sys
from random import randint


def find_max_crossing_subarray(a, low, mid, high):
    """
    Helper function for find_max_subarray()
    """
    left_sum = right_sum = -sys.maxsize
    max_left = max_right = int()
    s = 0

    for i in range(mid, low - 1, -1):
        s += a[i]
        if s > left_sum:
            left_sum = s
            max_left = i

    s = 0
    for j in range(mid + 1, high + 1):
        s += a[j]
        if s > right_sum:
            right_sum = s
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_max_subarray(a, low, high):
    """
    The book's O(NlogN) approach to solving the max subarray problem.
    :param a: (List) of Ints to search
    :param low: (Int) Starting index
    :param high: (Int) Ending index
    :return: (Tuple) starting index, ending index, and sum of the max subarray of A.
    """
    if high == low:
        return low, high, a[low]  # base case: only one element

    mid = (low + high) // 2
    left_low, left_high, left_sum = find_max_subarray(a, low, mid)
    right_low, right_high, right_sum = find_max_subarray(a, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, low, mid, high)

    if (left_sum >= right_sum) and (left_sum >= cross_sum):
        return left_low, left_high, left_sum
    elif (right_sum >= left_sum) and (right_sum >= cross_sum):
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def brute_force_max_subarray(a):
    """
    O(N^2) Approach to solving the max subarray problem.
    :param a: (List) of Ints to search
    :return: (Tuple) starting index, ending index, and sum of the max subarray of A.
    """
    n = len(a)
    low = high = int()
    max_sum = -sys.maxsize

    for i in range(0, n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s > max_sum:
                max_sum = s
                low, high = i, j

    return low, high, max_sum


def main():
    print('n items', '\t', 'time (s)')
    for i in range(100, 10001, 500):
        arr = [randint(-1000, 1001) for _ in range(i)]
        n = len(arr)
        start_time = time.perf_counter()
        find_max_subarray(arr, 0, n-1)
        # brute_force_max_subarray(arr)
        delta = time.perf_counter() - start_time

        print(n, '\t', delta)


if __name__ == '__main__':
    main()
