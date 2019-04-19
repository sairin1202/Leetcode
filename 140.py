from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.hash_map = {}


    def helper(self, s, wordDict):
        if len(s) == 0:
            return [[]], 1
        arrays = []
        for word in wordDict:
            if len(s) < len(word):
                continue
            if s[:len(word)] == word:
                if s[len(word):] in self.hash_map:
                    array, res = self.hash_map[s[len(word):]]
                else:
                    array, res = self.helper(s[len(word):], wordDict)
                    self.hash_map[s[len(word):]] = (deepcopy(array), res)
                if res == 1:
                    for a in array:
                        t = a[:]
                        t.insert(0, word)
                        arrays.append(t)
        if len(arrays) == 0:
            return [[]], 0
        return arrays, 1



    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = sorted(wordDict, key = lambda x: len(x))
        array, res = self.helper(s, wordDict)
        if res == 0:
            return []
        for i in range(len(array)):
            array[i] = " ".join(array[i])
        return array
