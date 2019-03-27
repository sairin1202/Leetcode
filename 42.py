class Solution(object):

    # def trap(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     sum_ = 0
    #     while(1):
    #         min_ = 10000000000
    #         idx1 = -1
    #         dis = 0
    #         for i, num in enumerate(height):
    #             if num > 0:
    #                 if num < min_:
    #                     min_ = num
    #                 if idx1 == -1:
    #                     idx1 = i
    #                 else :
    #                     dis += i-idx1-1
    #                     idx1 = i
    #         sum_ += dis*min_
    #         if idx1 == -1:
    #             return sum_
    #         # print(sum_)
    #         for i in range(len(height)):
    #             if height[i] > 0:
    #                 height[i] -= min_

        def trap(self, height):
            """
            :type height: List[int]
            :rtype: int
            """
            left = []
            right = []
            cur = 0
            for i, num in enumerate(height):
                if num > cur:
                    left.append(num)
                    cur = num
                else:
                    left.append(cur)
            cur = 0
            for i in range(len(height)-1, -1, -1):
                if height[i] > cur:
                    right.insert(0, height[i])
                    cur = height[i]
                else:
                    right.insert(0, cur)
            sum_ = 0
            # print(left)
            # print(right)
            for i in range(len(height)):
                sum_ += min(left[i], right[i]) - height[i]
            return sum_
