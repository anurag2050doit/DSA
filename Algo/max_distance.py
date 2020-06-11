class IndexArray:
    def __init__(self, val, index):
        self.val = val
        self.index = index

    def __str__(self):
        return self.val

    def __unicode__(self):
        return self.val



class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        sorted_arr = [IndexArray(x, pos) for pos, x in enumerate(A)]
        sorted_arr.sort(key=lambda i: i.val)
        print(sorted_arr)


if __name__ == '__main__':
    obj = Solution()
    obj.maximumGap([3, 5, 4, 2])
