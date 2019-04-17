class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        if len(prices) <= 1:
            return 0
        stack = [prices[0]]
        for i in range(1, len(prices)):
            if len(stack) != 0 and prices[i] <= stack[-1]:
                if len(stack) >= 1:
                    res += stack[-1] - stack[0]
                stack = [prices[i]]
            else:
                stack.append(prices[i])
        if len(stack) >= 2:
            res += stack[-1] - stack[0]
        return res
