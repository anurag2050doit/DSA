"""
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than
 O(n) space and traversing the stream sequentially O(1) times.

 Sample Input:
 [3 4 1 4 1]

 Sample Output:
 1

REF: https://www.interviewbit.com/problems/find-duplicate-in-array/
"""


def find_duplicate(arr):
    unique_dict = dict()
    for n in arr:
        if unique_dict.get(n):
            return 1
        unique_dict[n] = 1
    return -1


if __name__ == '__main__':
    print(find_duplicate([3, 4, 1, 4, 1]))
    print(find_duplicate([3, 2, 9, 6, 1]))
