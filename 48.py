class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2):
            for j in range(0, len(matrix[0])-i*2-1):
                temp = matrix[i][i+j]
                for m in range(4):
                    if m == 0:
                        # print(i+j, len(matrix[0])-i-1)
                        temp2 = matrix[i+j][len(matrix[0])-i-1]
                        matrix[i+j][len(matrix[0])-i-1] = temp
                        temp = temp2
                    elif m == 1:
                        # print(len(matrix)-1-i, len(matrix[0])-i-1-j)
                        temp2 = matrix[len(matrix)-1-i][len(matrix[0])-i-1-j]
                        matrix[len(matrix)-1-i][len(matrix[0])-i-1-j] = temp
                        temp = temp2
                    elif m == 2:
                        # print(len(matrix)-i-1-j, i)
                        temp2 = matrix[len(matrix)-i-1-j][i]
                        matrix[len(matrix)-i-1-j][i] = temp
                        temp = temp2
                    elif m == 3:
                        matrix[i][i+j] = temp
            # print(matrix)
        
