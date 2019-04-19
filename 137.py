class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = 0
        a = 0
        for num in nums:
            b = b ^ num & (~a)
            a = a ^ num & (~b)
        return b
