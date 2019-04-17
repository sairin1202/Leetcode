class Solution(object):
    def helper(self, board, x, y, mat):
        if x - 1 > 0:
            if board[x-1][y] == "O" and mat[x-1][y] == 0:
                mat[x-1][y] = 1
                self.helper(board, x-1, y, mat)
        if x + 1 < len(board):
            if board[x+1][y] == "O" and mat[x+1][y] == 0:
                mat[x+1][y] = 1
                self.helper(board, x+1, y, mat)
        if y - 1 > 0:
            if board[x][y-1] == "O" and mat[x][y-1] == 0:
                mat[x][y-1] = 1
                self.helper(board, x, y-1, mat)
        if y + 1 < len(board[0]):
            if board[x][y+1] == "O" and mat[x][y+1] == 0:
                mat[x][y+1] = 1
                self.helper(board, x, y+1, mat)
        return


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return 0
        mat = [[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board[0])):
            if board[0][i] == "O":
                mat[0][i] = 1
                self.helper(board, 0, i, mat)
        # print(mat)
        for i in range(len(board[0])):
            if board[-1][i] == "O":
                mat[-1][i] = 1
                self.helper(board, len(board)-1, i, mat)
        # print(mat)
        for i in range(len(board)):
            if board[i][0] == "O":
                mat[i][0] = 1
                self.helper(board, i, 0, mat)
        # print(mat)
        for i in range(len(board)):
            if board[i][-1] == "O":
                mat[i][-1] = 1
                self.helper(board, i, len(board[0])-1, mat)
        # print(mat)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and mat[i][j] == 0:
                    board[i][j] = "X"

        # print(mat)


                
