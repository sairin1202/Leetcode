class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        lowest = nums[0]
        highest = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            high = max(highest * nums[i], lowest * nums[i], nums[i])
            low = min(lowest * nums[i], highest * nums[i], nums[i])
            highest = high
            lowest = low
            res = max(res, highest)
            # print(highest, lowest)
        return res

            
