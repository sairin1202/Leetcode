class Solution(object):
    def exist_(self, board, word, idx, i, j, mat):
        if idx == len(word):
            return True

        if j+1 < len(board[0]) and board[i][j+1] == word[idx] and mat[i][j+1] == 0:
            mat[i][j+1] = 1
            res = self.exist_(board, word, idx+1, i, j+1, mat)
            mat[i][j+1] = 0
            if res == True:
                return True
        if i+1 < len(board) and board[i+1][j] == word[idx] and mat[i+1][j] == 0:
            mat[i+1][j] = 1
            res = self.exist_(board, word, idx+1, i+1, j, mat)
            mat[i+1][j] = 0
            if res == True:
                return True
        if j-1 >= 0 and board[i][j-1] == word[idx] and mat[i][j-1] == 0:
            mat[i][j-1] = 1
            res = self.exist_(board, word, idx+1, i, j-1, mat)
            mat[i][j-1] = 0
            if res == True:
                return True
        if i-1 >= 0 and board[i-1][j] == word[idx] and mat[i-1][j] == 0:
            mat[i-1][j] = 1
            res = self.exist_(board, word, idx+1, i-1, j, mat)
            mat[i-1][j] = 0
            if res == True:
                return True
        return False



    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        mat = [[0]*len(board[0]) for _ in range(len(board))]
        start = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == start:
                    mat[i][j] = 1
                    res = self.exist_(board, word, 1, i, j, mat)
                    if res == True:
                        return True
                    mat[i][j] = 0
        return False
