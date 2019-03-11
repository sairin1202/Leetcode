class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # let num1 short array
        # let num2 long array
        if len(nums1) > len(nums2):
            tmp = nums1[:]
            nums1 = nums2[:]
            nums2 = tmp
        len1 = len(nums1)
        len2 = len(nums2)
        left = -1
        right = len1
        p_x1 = (left + right) // 2
        p_x2 = p_x1 + 1
        p_y1 = (len1 + len2) // 2 - (p_x2) - 1
        p_y2 = p_y1 + 1

        x1 = nums1[p_x1] if p_x1 >= 0 else float('-inf')
        x2 = nums1[p_x2] if p_x2 < len1 else float('inf')
        y1 = nums2[p_y1] if p_y1 >= 0 else float('-inf')
        y2 = nums2[p_y2] if p_y2 < len2 else float('inf')

        while not (x1 <= y2 and y1 <= x2):
            if x1 > y2:
                right = p_x2 - 1
            elif y1 > x2:
                left = p_x1 + 1

            p_x1 = (left + right) // 2
            p_x2 = p_x1 + 1
            p_y1 = (len1 + len2) // 2 - (p_x2) - 1
            p_y2 = p_y1 + 1
            x2 = nums1[p_x2] if p_x2 < len1 else float('inf')
            x1 = nums1[p_x1] if p_x1 >= 0 else float('-inf')
            y2 = nums2[p_y2] if p_y2 < len2 else float('inf')
            y1 = nums2[p_y1] if p_y1 >= 0 else float('-inf')

        if (len1 + len2) % 2 == 0:
            return (max(x1, y1) + min(x2, y2)) / 2.0
        else:
            return min(x2, y2)