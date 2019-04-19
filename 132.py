class Solution(object):
    def __init__(self):
        self.hash_table = {}

    def helper(self, s):
        if s in self.hash_table:
            return self.hash_table[s]
        if len(s) < 1:
            return 0
        if len(s) == 1:
            return 1
        res = float("inf")
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                next_res = self.helper(s[i:])
                res = min(res, next_res+1)
        self.hash_table[s] = res
        return res


    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.helper(s) - 1
        
