class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[float("inf")]*len(triangle) for _ in range(len(triangle)+1)]
        for i in range(len(triangle)):
            dp[0][i] = 0
        for i in range(1, len(triangle)+1):
            for j in range(len(triangle[i-1])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i-1][j]
        return min(dp[-1])
        
