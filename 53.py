class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = float('-inf')
        pre = 0
        for num in nums:
            if pre >= 0:
                if pre+num > max_:
                    max_ = pre+num
                    pre = max_
                else:
                    pre = pre+num
            else:
                pre = num
                if num > max_:
                    max_ = num
        return max_
