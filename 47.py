from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.res = []

    def help(self, nums, start, end, target):
        if end == len(nums):
            return False
        for j in range(start, end):
            if target == nums[j]:
                return True
        return False

    def permute_(self, nums, idx):
        if idx == len(nums):
            nums_c = deepcopy(nums)
            self.res.append(nums_c)
            return
        for i in range(idx, len(nums)):
            if self.help(nums, idx, i, nums[i]) == False:
                nums[i], nums[idx] = nums[idx], nums[i]
                self.permute_(nums, idx+1)
                nums[i], nums[idx] = nums[idx], nums[i]


    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permute_(nums, 0)
        return self.res
