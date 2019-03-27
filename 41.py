class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 1

        for i in range(len(nums)):
            if nums[i] <= 0 :
                nums[i] = 1
            if nums[i] > len(nums):
                nums[i] = 1

        print(nums)
        for i in range(len(nums)):
            if nums[i] < len(nums):
                temp = nums[i] if nums[i]>0 else -1*nums[i]
                if temp < len(nums):
                    if nums[temp] > 0:
                        nums[temp] *= -1


        print(nums)
        for i in range(2, len(nums)):
            if nums[i] > 0:
                return i

        return len(nums)+1
