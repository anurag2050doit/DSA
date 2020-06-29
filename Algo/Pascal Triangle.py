"""
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        lisa = [[1]]
        for i in range(A):
            lisa.append(lisa)
            lisan = lisa[:]
            lisan.insert(0, 0)
            for i in range(len(lisa)):
                lisan[i] = lisa[i] + lisan[i]
            lisa = lisan[:]
