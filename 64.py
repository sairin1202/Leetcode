from copy import deepcopy
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mat = deepcopy(grid)
        for i in range(1, len(grid)):
            mat[i][0] = mat[i-1][0]+grid[i][0]
        for j in range(1, len(grid[0])):
            mat[0][j] = mat[0][j-1]+grid[0][j]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                mat[i][j] = min(mat[i-1][j], mat[i][j-1]) + grid[i][j]
        # print(mat)
        return mat[-1][-1]
