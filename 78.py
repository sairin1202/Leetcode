class Solution(object):
    def __init__(self):
        self.res = [[]]

    def subsets_(self, idx, nums, arr):
        if idx == len(nums):
            return
        for i in range(idx, len(nums)):
            arr.append(nums[i])
            self.res.append(arr[:])
            self.subsets_(i+1, nums, arr)
            arr.pop()
        return


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.subsets_(0, nums, [])
        return self.res
        
