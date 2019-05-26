"""

GFG: https://www.geeksforgeeks.org/binary-search/
"""


def binarySearch(array, lower, high, element):
    if high >= lower:

        mid = int(lower + (high - lower) / 2)

        if array[mid] == element:
            return mid

        if element > array[mid]:
            lower = mid
            return binarySearch(array, lower + 1, high, element)
        else:
            high = mid
            return binarySearch(array, lower, high - 1, element)

    else:
        return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    # Function call
    result = binarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
