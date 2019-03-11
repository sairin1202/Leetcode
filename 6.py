class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
#         # O(n^2)
#         if numRows == 1:
#             return s
#         if numRows >= len(s):
#             return s
#         mat = [[0]*(len(s)//2+1) for _ in range(numRows)]
#         direct = 1
#         cur_idx = (0,0)
#         for char in s:
#             mat[cur_idx[0]][cur_idx[1]] = char

#             if cur_idx[0] == numRows-1 and direct == 1:
#                 direct = 0
#             if cur_idx[0] == 0 and direct == 0:
#                 direct = 1

#             if direct == 1:
#                 cur_idx = (cur_idx[0]+1, cur_idx[1])
#             else:
#                 cur_idx = (cur_idx[0]-1, cur_idx[1]+1)
#         s = ""
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 if mat[i][j] != 0:
#                     s += mat[i][j]
#         return s



        # O(n)
        if numRows == 1:
            return s
        if numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]

        direct = 1
        cur_idx = 0
        for char in s:
            rows[cur_idx].append(char)
            if cur_idx == numRows-1 and direct == 1:
                direct = 0
            if cur_idx == 0 and direct == 0:
                direct = 1

            if direct == 1:
                cur_idx = cur_idx+1
            else:
                cur_idx = cur_idx-1

        s = ""
        for row in rows:
            s += "".join(row)
        return s


                
