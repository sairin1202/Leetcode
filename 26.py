class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        cur_num  = nums[0]
        count = 1
        idx = 1
        while idx < len(nums):
            if nums[idx] != cur_num:
                cur_num = nums[idx]
                nums[count] = nums[idx]
                count += 1
            idx += 1
        return count
