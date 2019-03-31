class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        mat = [[0]*n  for _ in range(n)]
        res = [[0]*n  for _ in range(n)]
        mat[0][0] = 1
        res[0][0] = 1
        count = 2
        direction = 0
        i = 0
        j = 0
        while count < n*n+1:
            if direction == 0:
                res[i][j+1] = count
                mat[i][j+1] = 1
                j += 1
                if j+1 >= n or mat[i][j+1] == 1:
                    direction = (direction+1)%4
            elif direction == 1:
                res[i+1][j] = count
                mat[i+1][j] = 1
                i += 1
                if i+1 >= n or mat[i+1][j] == 1:
                    direction = (direction+1)%4
            elif direction == 2:
                res[i][j-1] = count
                mat[i][j-1] = 1
                j -= 1
                if j-1 < 0 or mat[i][j-1] == 1:
                    direction = (direction+1)%4
            elif direction == 3:
                res[i-1][j] = count
                mat[i-1][j] = 1
                i -= 1
                if i-1 < 0 or mat[i-1][j] == 1:
                    direction = (direction+1)%4
            count += 1
            # print(res)
        return res
