class Solution(object):
    def __init__(self):
        self.res = []

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        count = 0
        direction = 0
        mat = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        res = []
        i = 0
        j = 0
        self.res.append(matrix[0][0])
        mat[i][j] = 1
        while count < len(matrix)*len(matrix[0])-1:
            if direction == 0:
                while j+1 < len(matrix[0]) and mat[i][j+1] != 1 :
                    mat[i][j] = 1
                    j+=1
                    count += 1
                    self.res.append(matrix[i][j])
                direction = (direction+1)%4
            if direction == 1:
                while i+1 < len(matrix) and mat[i+1][j] != 1 :
                    mat[i][j] = 1
                    i+=1
                    count += 1
                    self.res.append(matrix[i][j])
                direction = (direction+1)%4
            if direction == 2:
                while j-1 >= 0 and mat[i][j-1] != 1 :
                    mat[i][j] = 1
                    j-=1
                    count += 1
                    self.res.append(matrix[i][j])
                direction = (direction+1)%4
            if direction == 3:
                while i-1 >= 0 and mat[i-1][j] != 1 :
                    mat[i][j] = 1
                    i-=1
                    count += 1
                    self.res.append(matrix[i][j])
                direction = (direction+1)%4
        return self.res
