"""
Find the contiguous subarray within an array, A of length N which has the largest sum.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer representing the maximum possible sum of the contiguous subarray.
Constraints:

1 <= N <= 1e6
-1000 <= A[i] <= 1000
For example:

Input 1:
    A = [1, 2, 3, 4, -10]

Output 1:
    10

Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2:
    6

Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.

REF: https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
"""

inf = float('inf')


# Solution 1
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum = -inf
        sum_of_arr = 0
        for i in A:
            sum_of_arr = sum_of_arr + i
            if i > sum_of_arr and i > max_sum:
                sum_of_arr = i
                max_sum = i
            elif i > sum_of_arr:
                sum_of_arr = i
            if sum_of_arr > max_sum:
                max_sum = sum_of_arr
        return max_sum


# Solution 2

class Solution2:
    def maxSubArray(self, A):
        best = -inf
        sum_of_arr = 0
        for i in A:
            sum_of_arr += i
            best = max(sum_of_arr, best)
            sum_of_arr = max(sum_of_arr, 0)
        return best


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSubArray([-163, -20]))
    obj2 = Solution2()
    print(obj.maxSubArray([1, 2, 3, 4, -10]))
    print(obj.maxSubArray([-163, -20]))
    print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
