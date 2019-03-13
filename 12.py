class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sv = {"I":1 , "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}
        res = 0
        for i, char in enumerate(s):
            if i + 1 < len(s) and sv[s[i+1]] > sv[char]:
                res += sv[char] * -1
            else:
                res += sv[char]
        return res
