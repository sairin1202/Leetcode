class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        count = 0
        for i in range(len(nums)):
            if count == 0:
                count += 1
                cur = nums[i]
            elif cur == nums[i]:
                count += 1
            else:
                count -= 1
        return cur
