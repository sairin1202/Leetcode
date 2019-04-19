class Solution(object):
    def __init__(self):
        self.hash_map = {}

    def helper(self, s, wordDict):
        if len(s) == 0:
            return True
        for i, word in enumerate(wordDict):
            if len(s) < len(word):
                continue
            if word == s[:len(word)]:
                if s[len(word):] in self.hash_map:
                    res = self.hash_map[s[len(word):]]
                else:
                    res = self.helper(s[len(word):], wordDict)
                    self.hash_map[s[len(word):]] = res
                if res:
                    return True
        return False


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = sorted(wordDict, key = lambda x: -len(x))
        return self.helper(s, wordDict)
        
