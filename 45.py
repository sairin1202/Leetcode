class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        idx = 0
        cur_max_bound = nums[0]
        count = 0
        while cur_max_bound < len(nums)-1:
            count += 1
            max_idx = idx
            for i in range(idx+1, cur_max_bound+1):
                if nums[i] + i > cur_max_bound:
                    cur_max_bound = nums[i] + i
                    max_id = i
            idx = max_id
            # print(idx, cur_max_bound)
        return count+1




        
