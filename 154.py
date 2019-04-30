class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        flag = 0
        cur_num  = nums[0]
        for num in nums:
            if num != cur_num:
                flag = 1
        if flag == 0:
            return cur_num


        for i in range(len(nums)):
            if nums[i] != nums[len(nums)-1-i]:
                nums = nums[i:len(nums)-i]
                break
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return min(cur_num, nums[left])
