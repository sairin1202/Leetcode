class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        stack = []
        res = 0
        least = prices[0]
        for i in range(1, len(prices)):
            if least > prices[i]:
                least = prices[i]
            else:
                if prices[i] - least > res:
                    res = prices[i] - least
        return res


        
