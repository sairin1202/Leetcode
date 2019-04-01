class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        mat = [[0]*(m+1) for _ in range(n+1)]
        if obstacleGrid[0][0] == 1:
            mat[1][1] = 0
        else:
            mat[1][1] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 and j ==1:
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    mat[i][j] = 0
                else:
                    mat[i][j] = mat[i-1][j] + mat[i][j-1]
        return mat[n][m]
