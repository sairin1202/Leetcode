class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        boarder = nums[0]
        for i in range(1, len(nums)):
            if i <= boarder:
                if i+nums[i] > boarder:
                    boarder = i+nums[i]
                    if boarder >= len(nums)-1:
                        return True
            else:
                return False

        return True
