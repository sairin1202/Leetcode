class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = 10000
        res = 100000
        for i, num in enumerate(nums):
            start = i+1
            end = len(nums)-1
            while start < end:
                cur = num + nums[start] + nums[end]
                if cur == target:
                    return target
                if cur > target:
                    end -= 1
                if cur < target:
                    start += 1
                if abs(cur - target) < closest:
                    closest = abs(cur - target)
                    res = cur
        return res

                    
