class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        height = [0]*n
        left = [0]*n
        right = [n-1]*n
        max_ = 0
        for i in range(m):
            cur_left = 0
            cur_right = n-1
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], cur_left)
                else:
                    cur_left = j+1
                    left[j] = 0
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    cur_right = j-1
                    right[j] = n-1
            for j in range(n):
                if (right[j]-left[j]+1)*height[j] > max_:
                    max_ = (right[j]-left[j]+1)*height[j]
        return max_
