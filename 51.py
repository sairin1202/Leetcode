from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.res = []


    def valid(self, array, idx, value):
        for i in range(0, idx):
            if value == array[i]:
                return False
            if value - array[i] == idx - i:
                return False
            if value - array[i] == i - idx:
                return False
        return True

    def solveNQueens_(self, n, idx, array):
        if idx >= n:
            self.res.append(deepcopy(array))
            return
        for i in range(n):
            array[idx] = i
            if self.valid(array, idx, i):
                self.solveNQueens_(n, idx+1, array)

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        output = []
        array = [0]*n
        self.solveNQueens_(n, 0, array)
        for res in self.res:
            tmp = []
            for num in res:
                string = "."*(n-1)
                string = string[:num]+"Q"+string[num:]
                tmp.append(string)
            output.append(tmp)
        return output

        
