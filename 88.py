from copy import deepcopy
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num1_copy = deepcopy(nums1)
        idx1 = 0
        idx2 = 0
        while idx1 < m and idx2 < n:
            if num1_copy[idx1] < nums2[idx2]:
                nums1[idx1+idx2] = num1_copy[idx1]
                idx1 += 1
            else:
                nums1[idx1+idx2] = nums2[idx2]
                idx2 += 1

        if idx1 < m:
            while idx1 < m:
                nums1[idx1+idx2] = num1_copy[idx1]
                idx1 += 1

        if idx2 < n:
            while idx2 < n:
                nums1[idx1+idx2] = nums2[idx2]
                idx2 += 1


        
