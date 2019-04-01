class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (s[0] == "-" or s[0] == "+") and (s[1] == "-" or s[1] == "+"):
            return False
        try:
            float(s)
        except:
            return False
        return True
