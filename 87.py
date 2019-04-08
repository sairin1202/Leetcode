from collections import Counter
class Solution(object):
    def __init__(self):
        self.hash_map = {}

    def Scramble(self, s1, s2):
        if s1+"#"+s2 in self.hash_map:
            return True
        # print(s1,s2)
        if Counter(s1) != Counter(s2):
            return False
        if s1 == s2:
            return True

        for i in range(1, len(s1)):
            res = (self.Scramble(s1[:i], s2[:i]) and self.Scramble(s1[i:], s2[i:])) or (self.Scramble(s1[:i], s2[len(s2)-i:]) and self.Scramble(s1[i:], s2[:len(s2)-i]))
            if res:
                self.hash_map[s1+"#"+s2] = 1
                return True
        return False

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return self.Scramble(s1, s2)



        
