class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        left = 0
        right = len(heights)-1
        ans = float("-inf")
        while left <= right:
            cur = min(heights[left], heights[right])*(right - left + 1)
            print(cur)
            if cur > ans:
                ans = cur
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return ans

        
