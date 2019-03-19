class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        dp = [0]*(len(s)+1)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
                dp[i+1] = 0
            elif c == ")":
                if len(stack) == 0:
                    dp[i+1] = 0
                else:
                    j = stack.pop()
                    dp[i+1] = i - j + 1 + dp[j]
            else:
                dp[i+1] = 0
        # print(dp)
        return max(dp)

        
