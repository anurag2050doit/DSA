"""
Largest Sum Contiguous Subarray
Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has
the largest sum.

GFG: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

"""


def max_sub_array_sum(array):
    max_sub = 0
    initial_pos = 0
    for i in range(1, len(array)):
        sum_array = sum(array[initial_pos:i])
        if sum_array > max_sub:
            max_sub = sum_array
            initial_pos = i - 1
        if sum_array < 0:
            initial_pos = i
    return max_sub


if __name__ == '__main__':
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    result = max_sub_array_sum(a)
    print(result)
