class Solution(object):
    def helper(self, s):
        if len(s) < 1:
            return [[]]
        if len(s) == 1:
            return [s[:]]
        res = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                next_res = self.helper(s[i:])
                for r in next_res:
                    temp = [s[:i]]
                    temp.extend(r)
                    res.append(temp)
        return res

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return self.helper(s)
