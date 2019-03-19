class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # find first decrease number
        idx1 = 0
        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                idx1 = 0
                break
            if nums[i] > nums[i-1]:
                idx1 = i
                break

        if idx1 > 0:
            # find first number larger
            idx2 = idx1 - 1
            for i in range(idx1, len(nums)):
                if nums[idx2] >= nums[i]:
                    idx2 = i-1
                    break
            if idx2 == idx1 - 1:
                idx2 = len(nums) - 1
            nums[idx2], nums[idx1-1] = nums[idx1-1], nums[idx2]

#         print(idx1, idx2)
        # swap all number from idx1
        left = idx1
        right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

                
