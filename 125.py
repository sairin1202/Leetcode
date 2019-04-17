class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        while i < len(s):
            c = s[i]
            if "A" <= c <= "Z":
                c = chr(ord(c) - ord("A") + ord("a"))
                s = s[:i] + c + s[i+1:]
                i += 1
            elif "a" <= c <= "z" or "0" <= c <="9":
                i += 1
            else:
                s = s[:i] + s[i+1:]
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True
