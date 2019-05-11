class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        for j in range(len(s)-1, -1, -1):
            res += (ord(s[j])-ord("A")+1)*(26**i)
            i += 1
        return res
