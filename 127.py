class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)
        queue = [(endWord, 1)]

        wordSet = set(wordList)
        visited = set()
        visited.add(endWord)
        while len(queue):
            # print(queue)
            cur, level = queue.pop(0)
            temp = cur[:]
            for i in range(len(cur)):
                for j in range(26):
                    cur = cur[:i] + chr(ord("a")+j) + cur[i+1:]
                    if cur in wordSet and cur not in visited:
                        visited.add(cur)
                        queue.append((cur, level+1))

                        if cur == beginWord:
                            return level+1
                cur = temp
        return 0
        
