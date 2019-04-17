class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        lr = [0]*len(prices)
        low = prices[0]
        dif = 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                if prices[i] - low > dif:
                    dif = prices[i] - low
            lr[i] = dif
        rl = [0]*len(prices)
        high = prices[-1]
        dif = 0
        for i in range(len(prices)-2, -1, -1):
            if prices[i] > high:
                high = prices[i]
            else:
                if high - prices[i] > dif:
                    dif = high - prices[i]
            rl[i] = dif
        # print(lr)
        # print(rl)
        res = 0
        for i in range(1,len(prices)):
            if lr[i] + rl[i] > res:
                res = lr[i] + rl[i]
        return res
        
