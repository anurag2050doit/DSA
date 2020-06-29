"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""


class K:
    def __init__(self, obj, *args):
        self.obj = obj

    def __lt__(self, other):
        return '%d%d' % (self.obj, other.obj) < '%d%d' % (other.obj, self.obj)


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        return str(int(''.join([str(s) for s in A])))
