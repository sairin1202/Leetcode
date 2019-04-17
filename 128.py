''class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        count = 1
        res = 1
        for num in nums:
            if num-1 in numSet:
                count = 1
            else:
                count = 1
                while num+1 in numSet:
                    count += 1
                    num += 1
                    # print("num",count)
                res = max(res, count)
        return res
        
