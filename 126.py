from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.res = []
        self.target_level = -1

    def dfs(self, root, visited, hash_table, target, res, levels):
        if len(res) >= len(levels):
            return
        for word in levels[len(res)]:
            if word in hash_table[root]:
                if word == target:
                    res.append(target)
                    self.res.append(res[::-1])
                    res.pop()
                    return
                if visited[word] == 0:
                    visited[word] = 1
                    res.append(word)
                    self.dfs(word, visited, hash_table, target, res, levels)
                    visited[word] = 0
                    res.pop()
        return

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return []

        wordSet = set(wordList)

        hash_table = {}
        hash_table[endWord] = []
        queue = [(endWord,0)]
        bfs_visit = set()
        bfs_visit.add(endWord)
        levels = []
        cur_level = -1
        level_l = [endWord]

        while len(queue):
            cur, level = queue.pop(0)
            if level != cur_level:
                cur_level = level
                levels.append(level_l[:])
                level_l = []
            if cur == beginWord:
                levels.pop()
                levels.append([beginWord])
                target_level = level
                break
            temp = cur[:]
            for i in range(len(cur)):
                for j in range(26):
                    cur = cur[:i] + chr(ord("a")+j) + cur[i+1:]
                    if cur == beginWord:
                        self.target_level = level
                    if cur == temp:
                        continue
                    if cur in wordSet:
                        if temp not in hash_table:
                            hash_table[temp] = [cur]
                        else:
                            hash_table[temp].append(cur)
                        if cur not in bfs_visit:
                            bfs_visit.add(cur)
                            queue.append((cur, level+1))
                            level_l.append(cur)
                            hash_table[cur] = []
                cur = cur[:i] + temp[i] + cur[i+1:]

        if self.target_level == -1:
            return []
        # print(target_level)
        # print(levels)
        # print(hash_table)
        res = [endWord]
        visited = {}
        for l in levels:
            for word in l:
                visited[word] = 0
        visited[endWord] = 1
        self.dfs(endWord, visited, hash_table, beginWord, res, levels)
        return self.res

        
