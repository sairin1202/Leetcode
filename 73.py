class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix[0])
        height = len(matrix)
        mat = [[1]*width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    for m in range(width):
                        mat[i][m] = 0
                    for m in range(height):
                        mat[m][j] = 0
        for i in range(height):
            for j in range(width):
                matrix[i][j] *= mat[i][j]
        return matrix
