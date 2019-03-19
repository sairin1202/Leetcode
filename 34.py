class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        left_idx = left
        # print(left,left_idx)
        if left_idx >= len(nums):
            return [-1, -1]
        if nums[left_idx] != target:
            return [-1, -1]

        left = left_idx
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        right_idx = right
        # print(right, right_idx)
        if right < len(nums) - 1:
            if nums[right_idx] != target:
                return [left_idx, left_idx]

        return [left_idx, right_idx]


        
