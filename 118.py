class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        triangle = [[1],[1,1]]
        for i in range(2, numRows):
            res = [1]
            for j in range(i-1):
                res.append(triangle[-1][j] + triangle[-1][j+1])
            res.append(1)
            triangle.append(res)
        return triangle
                
