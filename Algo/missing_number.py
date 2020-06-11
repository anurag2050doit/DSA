"""
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3]

Output:[3, 4]

A = 3, B = 4
"""


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        total_number = len(A)
        sum_of_number = (total_number * (total_number + 1)) / 2
        unique_dict = dict()
        repeating, missing = None, None
        sum_of_arr = 0
        for n in A:
            if unique_dict.get(n):
                repeating = n
            else:
                unique_dict[n] = 1
                sum_of_arr += n
        missing = sum_of_number - sum_of_arr
        return repeating, missing


if __name__ == '__main__':
    obj = Solution()
    print(obj.repeatedNumber([3, 1, 2, 5, 3]))
