"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        search_hash = dict()
        for p, v in enumerate(nums):
            if v > target:
                continue
            diff = target - v
            if search_hash.get(diff) is not None:
                return [search_hash[diff], p]
            else:
                search_hash[v] = p


if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum([3, 2, 4], 6))
