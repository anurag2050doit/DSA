"""
Write a program to print all permutations of a given string
A permutation, also called an “arrangement number” or “order,”
is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself.
 A string of length n has n! permutation.
Source: Mathword(http://mathworld.wolfram.com/Permutation.html)

Below are the permutations of string ABC.
ABC ACB BAC BCA CBA CAB

GFG: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
"""


def to_string(string_list):
    return ''.join(string_list)


def string_per(string, l, r):
    if l == r:
        print(to_string(string))
    else:
        for i in range(l, r + 1):
            string[l], string[i] = string[i], string[l]
            string_per(string, l + 1, r)
            string[l], string[i] = string[i], string[l]


if __name__ == '__main__':
    string = "ABC"
    n = len(string)
    a = list(string)
    string_per(a, 0, n-1)