class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
#         dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
#         for i in range(len(s)+1):
#             dp[0][i] = i
#         for i in range(len(t)+1):
#             dp[i][0] = i

#         for i in range(1, len(t)+1):
#             for j in range(1, len(s)+1):
#                 ti = i-1
#                 sj = j-1
#                 if t[ti] == s[sj]:
#                     dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
#                 else:
#                     dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
#         return dp[-1][-1] == 1
        if abs(len(s) - len(t)) > 1:
            return False
        sidx = 0
        tidx = 0
        distance = 0
        if len(s) - len(t) == 1:
            if len(t) == 0:
                return True
            while sidx < len(s) and tidx < len(t):
                if distance > 1:
                    return False
                if s[sidx] == t[tidx]:
                    sidx += 1
                    tidx += 1
                else:
                    distance +=1
                    sidx += 1
            distance += len(s) - sidx + len(t) - tidx
            if distance != 1:
                return False
        if len(t) - len(s) == 1:
            if len(s) == 0:
                return True
            while sidx < len(s) and tidx < len(t):
                if distance > 1:
                    return False
                if s[sidx] == t[tidx]:
                    sidx += 1
                    tidx += 1
                else:
                    distance +=1
                    tidx += 1
            distance += len(s) - sidx + len(t) - tidx
            if distance != 1:
                return False
        if len(t) == len(s):
            if len(t) == 0:
                return False
            while sidx < len(s) and tidx < len(t):
                if distance > 1:
                    return False
                if s[sidx] != t[tidx]:
                    distance += 1
                sidx += 1
                tidx += 1
            if distance != 1:
                return False
        return True
