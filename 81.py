class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums)-1
        while left < right and nums[left] == nums[right]:
            left += 1

        while  left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return True
            elif target < nums[mid]:
                if target >= nums[left]:
                    right = mid - 1
                elif target <= nums[right] and nums[mid] <= nums[right]:
                    right = mid - 1
                elif target <= nums[right] and nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    return False
            else:
                if target >= nums[left] and nums[mid] < nums[left]:
                    right = mid - 1
                elif target >= nums[left] and nums[mid] >= nums[left]:
                    left = mid + 1
                elif target <= nums[right]:
                    left = mid + 1
                else:
                    return False
        return False
