
class Solution(object):
    def __init__(self):
        self.res = []

    def combine_(self, idx, n, k, arr):
        if len(arr) == k:
            # print(arr)
            self.res.append(arr[:])
        if idx >= n+1:
            return
        for i in range(idx, n+1):
            arr.append(i)
            self.combine_(i+1, n, k, arr)
            arr.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.combine_(1, n, k, [])
        return self.res
        
