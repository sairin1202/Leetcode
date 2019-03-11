class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i, num in enumerate(nums):
            hash_table[num] = i
        for i, num in enumerate(nums):
            if target - num in hash_table and hash_table[target-num] != i:
                return [i, hash_table[target-num]]