class Solution(object):
    def __init__(self):
        self.res = [[]]

    def sub_(self, nums, index, res, left):
        appeared = set()
        for i in range(index, len(nums)):
            if nums[i] in appeared:
                continue
            appeared.add(nums[i])
            if len(res) == 0:
                left = i
            res.append(nums[i])
            self.res.append(res[:])
            self.sub_(nums, i+1, res, left)
            res.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.sub_(nums, 0, res, 0)
        return self.res
