# Python-Sorting-Algorithms

## Overview
This project does X.

## Section 1
### Part 1
This file showcases very particular implementations of MergeSort and Insertion-Sort, comparing their performance in a series of tests.  Each algorithm is first tested on randomly filled, unsorted arrays of sizes between 100 and 10000, with a step size of 250.  The algorithms are then tested under the same set of conditions, except that the lists are already sorted.

Results are provided in "Section1/Reporting/", including both the raw performance data in "graphs.xlsx", as well as graphs showing their growth rates in the "Image" folder.  The files "chart1" and "chart2" state the order of time required to run various different algorithms.

### Part 2
This file showcases two different solutions to the maximum subarray problem.  One solution uses recursion, along with a helper function, and is able to solve the problem in time order NlogN.  The other solution is a brute-force method that utilizes nested "for" loops, where the outer loop iterates through all possible starting indices and the inner loop iterates through all the possible ending indices.

Each solution is tested by measuring the amount of time it takes to solve lists of sizes between 100 and 10000, randomly filled with numbers between -1000 and 1000, and with a step size of 500.

Results are once again provided in "Section1/Reporting/", including performance data and growth rates.

## Section 2
### Part 1
An implementation of Heap-Sort which stores the binary heap with the root at index 1. The value at index 0 is ignored.  This function makes use of several helper functions, including parent, left, right, max_heapify, and build_max_heap.  The performance of this algorithm is then compared to that of Merge-Sort from Section 1, Part 1.  The test cases are randomly-generated lists of numbers.

Results for Parts 1-4 in Section 2 [all below] can be found in "Section2/Reporting/".

### Part 2
An implementation of Quicksort that utilizes the "Partition" helper function.  Randomly-generated arrays are used to compare its performance with both Mergesort and Heapsort.

### Part 3
Contains the previous implementations of Heap-Sort, Merge-Sort, and Quicksort, along with two modified versions of the Quicksort algorithm.  Randomized Quicksort picks a pivot point at random.  Median-of-Three Quicksort takes the first number in the list, the last number in the list, and the number in the middle of the list.  It then finds the median of those three values and uses it as the pivot.  The purpose of introducing these variations of Quicksort is to mitigate the algorithm's poor performance on lists that are already sorted.  All of these algorithms are tested on pre-sorted lists.

### Part 4
Contains only the quicksort algorithm and its two modified forms.  All of their performances are tested on both randomly-generated lists and completely sorted lists.

## Authors
* [Aaron Csetter](https://github.com/acsetter)
* [Ian Peña](https://github.com/IanP105)
* [Nathan Davis](https://github.com/NathanD11)
* [Dmytro Dobrynin](https://github.com/dimdbr)
