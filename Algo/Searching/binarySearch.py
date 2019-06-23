"""
Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of
the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until
the value is found or the interval is empty.


GFG: https://www.geeksforgeeks.org/binary-search/
"""


def binary_search(array, lower, high, element):
    if high >= lower:

        mid = int(lower + (high - lower) / 2)

        if array[mid] == element:
            return mid

        if element > array[mid]:
            lower = mid
            return binary_search(array, lower + 1, high, element)
        else:
            high = mid
            return binary_search(array, lower, high - 1, element)

    else:
        return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    # Function call
    result = binary_search(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
