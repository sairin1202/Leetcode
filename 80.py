from collections import Counter
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return len(nums)
        idx = 1
        count = 1
        current = nums[0]
        for i in range(1, len(nums)):

            if nums[i] == current:
                if count >= 2:
                    pass
                else:
                    count += 1
                    nums[i],nums[idx] = nums[idx],nums[i]
                    idx += 1
            else:
                current = nums[i]
                count = 1
                nums[i],nums[idx] = nums[idx],nums[i]
                idx += 1
            # print(nums)
        return idx



            
