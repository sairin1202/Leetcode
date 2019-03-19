class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[left]  <= nums[right]:
                if nums[mid] <target:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if target > nums[right] and target < nums[left]:
                    return -1
                if nums[mid] >= nums[left]:
                    if target > nums[mid]:
                        left = mid + 1
                    elif target < nums[mid] and target < nums[left]:
                        left = mid + 1
                    elif target < nums[mid] and target >= nums[left]:
                        right = mid - 1
                else:
                    if target >= nums[left]:
                        right = mid - 1
                    elif target <= nums[right] and target >nums[mid]:
                        left = mid + 1
                    elif target < nums[mid]:
                        right = mid - 1
            print(left,right)
        return -1
                        
