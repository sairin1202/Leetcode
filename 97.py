class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1)+len(s2):
            return False
        dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    if s3[j-1] == s1[j-1] and dp[i][j-1]:
                        dp[i][j] = True
                elif j == 0:
                    if s3[i-1] == s2[i-1] and dp[i-1][j]:
                        dp[i][j] = True
                else:
                    if s3[i+j-1] == s1[j-1] and dp[i][j-1]:
                        dp[i][j] = True
                    if s3[i+j-1] == s2[i-1] and dp[i-1][j]:
                        dp[i][j] = True
        # print(dp)
        return dp[-1][-1]
