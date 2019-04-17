class Solution(object):
    def __init__(self):
        self.hash = {}
        self.hash[0] = 1
        self.hash[1] = 1

    def numTrees_(self, start, end):
        if end - start <= 1:
            return 1
        if end - start in self.hash:
            return self.hash[end - start]
        count = 0
        for i in range(start, end):
            left = self.numTrees_(start, i)
            right = self.numTrees_(i+1, end)
            count += left*right
        self.hash[end - start] = count

        return count

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.numTrees_(1, n+1)
        # print(self.hash)
