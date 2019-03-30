from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.res = 0


    def valid(self, array, idx, value):
        for i in range(0, idx):
            if value == array[i]:
                return False
            if value - array[i] == idx - i:
                return False
            if value - array[i] == i - idx:
                return False
        return True

    def totalNQueens_(self, n, idx, array):
        if idx >= n:
            self.res += 1
            return
        for i in range(n):
            array[idx] = i
            if self.valid(array, idx, i):
                self.totalNQueens_(n, idx+1, array)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = []
        array = [0]*n
        self.totalNQueens_(n, 0, array)
        return self.res
        
