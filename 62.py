class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mat = [[0]*(m+1) for _ in range(n+1)]
        mat[1][1] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 and j ==1:
                    continue
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
        return mat[n][m]
