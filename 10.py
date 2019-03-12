# p.charAt(j) == s.charAt(i) : dp[i][j] = dp[i-1][j-1]
# If p.charAt(j) == ‘.’ : dp[i][j] = dp[i-1][j-1];
# If p.charAt(j) == ‘*’:
#     here are two sub conditions:
#     if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2] //in this case, a* only counts as empty
#     if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == ‘.’:
#         dp[i][j] = dp[i-1][j] //in this case, a* counts as multiple a 
#         dp[i][j] = dp[i][j-1] // in this case, a* counts as single a
#         dp[i][j] = dp[i][j-2] // in this case, a* counts as empty

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp = [[0]*(len(s)+1) for _ in range(len(p)+1)]
        dp[0][0] = 1
        for i in range(1,len(p)+1):
            if p[i-1] == "*":
                dp[i][0] = dp[i-2][0]
        for i in range(1,len(p)+1):
            for j in range(1,len(s)+1):
                if p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                if p[i-1] != s[j-1]:
                    dp[i][j] = 0
                if p[i-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                if p[i-1] == "*":
                    if p[i-2] == s[j-1] or p[i-2] == ".":
                        dp[i][j] = max(dp[i-1][j], dp[i-2][j], dp[i][j-1])
                    else:
                        dp[i][j] = dp[i-2][j]
        if dp[-1][-1] > 0:
            return True
        else:
            return False
