class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_hash_maps = [{} for i in range(9)]
        col_hash_maps = [{} for i in range(9)]
        block_hash_maps = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif not (board[i][j] <= "9" and board[i][j] >= "0"):
                    return False
                else:
                    if board[i][j] not in row_hash_maps[i]:
                        row_hash_maps[i][board[i][j]] = 1
                    else:
                        return False
                    if board[i][j] not in col_hash_maps[j]:
                        col_hash_maps[j][board[i][j]] = 1
                    else:
                        return False
                    if board[i][j] not in block_hash_maps[(i//3)*3+j//3]:
                        block_hash_maps[(i//3)*3+j//3][board[i][j]] = 1
                    else:
                        return False
                # print(row_hash_maps)
        return True
