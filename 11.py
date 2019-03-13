class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # brute force
        # 1 3 5 7 2 4 6
        # when calculate max capcity of height 6
        # find 1 3 5 6 and 7
#         max_ = 0

#         for idx in range(1, len(height)):
#             stack = []
#             for i in range(0, idx+1):
#                 if height[i] >= height[idx]:
#                     cur_max = height[idx]*(idx-i)
#                     if cur_max > max_:
#                         max_ = cur_max
#                 elif len(stack) == 0 or height[i] > stack[-1]:
#                     cur_max = height[i]*(idx-i)
#                     if cur_max > max_:
#                         max_ = cur_max
#                     stack.append(height[i])
#         return max_

        # two point
        max_ = 0
        left = 0
        right = len(height)-1
        while left < right:
            cur_cap = min(height[left], height[right]) * (right-left)
            if cur_cap > max_:
                max_ = cur_cap
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max_




        
