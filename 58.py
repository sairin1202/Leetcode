class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                s = s[:-1]
            else:
                break

        count = 0
        for c in s:
            if c == " ":
                count = 0
            else:
                count += 1

        return count
        
