from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.res = []


    def permute_(self, nums, idx):
        if idx == len(nums):
            nums_c = deepcopy(nums)
            self.res.append(nums_c)
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.permute_(nums, idx+1)
            nums[idx], nums[i] = nums[i], nums[idx]



    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permute_(nums, 0)
        return self.res
        
