class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[0]*(len(s)+1) for _ in range((len(p)+1))]
        dp[0][0] = 1
        for i in range(1, len(p)+1):
            for j in range(0, len(s)+1):
                if j == 0 and p[i-1] != "*":
                    dp[i][j] = 0
                    continue
                if p[i-1]== "*":
                    if dp[i-1][j] == 1 or dp[i][j-1] == 1:
                        dp[i][j] = 1
                elif p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 0
        # print(dp)
        if dp[-1][-1] == 1:
            return True
        else:
            return False
