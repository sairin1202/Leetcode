class Solution(object):
    def factorial(self, n):
        if n == 0:
            return 1
        return n*self.factorial(n-1)

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        res = [1]
        for i in range(rowIndex-1):
            res.append(self.factorial(rowIndex)//self.factorial(rowIndex-(i+1))//self.factorial(i+1))
        res.append(1)
        return res
