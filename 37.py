from copy import deepcopy

class Solution(object):

    def __init__(self):
        self.board = None
        self.relate = {}
        self.count= 0
    def solve_(self, board, idx, mat, visit):
        self.count+=1
        if idx == len(visit):
            self.board = board
            return 1

        row = visit[idx][0]
        col = visit[idx][1]

        for i in range(1,10):
            if mat[row][col][i] == 1:
                record = []
                for cor in self.relate[(row,col)]:
                    x = cor[0]
                    y = cor[1]
                    if mat[x][y][i] == 1:
                        record.append((x,y))
                    mat[x][y][i] = 0
                board[row][col] = str(i)
                if self.solve_(board, idx+1, mat, visit):
                    return 1
                for cor in record:
                    x = cor[0]
                    y = cor[1]
                    mat[x][y][i] = 1
        return 0


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        mat = [[[1]*10 for _ in range(9)] for _ in range(9)]
        visit = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    for m in range(9):
                        mat[i][m][int(board[i][j])] = 0
                    for m in range(9):
                        mat[m][j][int(board[i][j])] = 0
                    for m in range(3):
                        for n in range(3):
                            mat[i//3*3+m][j//3*3+n][int(board[i][j])] = 0
                else:
                    # record the place which need to replace
                    visit.append((i,j))
                    # record the place related to (i,j)
                    for x in range(j, 9):
                        if board[i][x] == ".":
                            if (i,j) not in self.relate:
                                self.relate[(i,j)] = [(i,x)]
                            else:
                                self.relate[(i,j)].append((i,x))
                    for y in range(i, 9):
                        if board[y][j] == ".":
                            if (i,j) not in self.relate:
                                self.relate[(i,j)] = [(y,j)]
                            else:
                                self.relate[(i,j)].append((y,j))
                    for m in range(3):
                        for n in range(3):
                            if board[i//3*3+m][j//3*3+n] == ".":
                                if (i,j) not in self.relate:
                                    self.relate[(i,j)] = [(i//3*3+m,j//3*3+n)]
                                else:
                                    self.relate[(i,j)].append((i//3*3+m,j//3*3+n))


        self.solve_(board, 0, mat, visit)
        for i in range(9):
            for j in range(9):
                board[i][j] = self.board[i][j]
