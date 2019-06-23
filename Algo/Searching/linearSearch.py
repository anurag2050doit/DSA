"""
Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.

https://www.geeksforgeeks.org/linear-search/

"""


def linear_search(arr, element):
    position = 0
    flag = False

    while position < len(arr) and not flag:
        if arr[position] == element:
            return position + 1
        else:
            position += 1

    return -1


array = [1, 5, 3, 19, 2, 23]
num = 5

pos = linear_search(array, num)

if pos == -1:
    print('Element not found')
else:
    print('Element found at %s' % pos)
