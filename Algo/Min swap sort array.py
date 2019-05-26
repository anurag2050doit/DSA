"""
Minimum number of swaps required to sort an array
Given an array of n distinct elements, find the minimum number of swaps required to sort the array.

GFG: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
HackerRank: https://www.hackerrank.com/challenges/minimum-swaps-2/problem
"""


def min_swap(array):
    swap = 0
    unsorted_arr_map = {p: v for (v, p) in enumerate(array, start=0)}
    sorted_arr = sorted(array)

    for correct_pos, element in enumerate(sorted_arr, start=0):
        pos = unsorted_arr_map[element]
        if pos != correct_pos:
            wrong_value = array[correct_pos]
            unsorted_arr_map[element] = correct_pos
            unsorted_arr_map[wrong_value] = pos
            array[correct_pos], array[pos] = element, wrong_value
            swap += 1

    return swap


if __name__ == '__main__':
    ar = [4, 3, 1, 2]
    print(min_swap(ar))
