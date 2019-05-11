class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        # get min and max
        min_ = float("inf")
        max_ = float("-inf")
        for i in range(len(nums)):
            if nums[i] < min_:
                min_ = nums[i]
            if nums[i] > max_:
                max_ = nums[i]
        if max_ - min_ == 0:
            return 0
        gaps = (max_-min_) // (len(nums)-1) + 1
        buckets = [[float("inf"), float("-inf"), 0] for _ in range(len(nums)+1)]
        for num in nums:
            b = (num - min_) // gaps
            if buckets[b][0] > num:
                buckets[b][0] = num
                buckets[b][2] = 1
            if buckets[b][1] < num:
                buckets[b][1] = num
                buckets[b][2] = 1
        # print(buckets)

        if len(buckets) == 0:
            return 0
        cur_max = buckets[0][0]
        max_gap = float("-inf")
        for i in range(len(buckets)):
            if buckets[i][2] == 1:
                max_gap = max(buckets[i][0] - cur_max, max_gap, buckets[i][1]- buckets[i][0])
                cur_max = buckets[i][1]
        return max_gap



            
