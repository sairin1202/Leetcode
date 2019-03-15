class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # same as 3Sum
        res= set()
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)-1):
                cur_sum = nums[i]+nums[j]
                start = j+1
                end = len(nums)-1
                while start < end:
                    if nums[start]+nums[end]+cur_sum > target:
                        end -= 1
                    elif nums[start]+nums[end]+cur_sum == target:
                        res.add((nums[i],nums[j],nums[start],nums[end]))
                        start += 1
                        end -= 1
                    else:
                        start += 1
        return list(res)
