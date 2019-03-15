from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.res = []

    def generateParenthesis_(self, c, cur, n, res):
        # c numbers of (
        # cur current length
        # n total number of (
        if cur > c*2:
            return
        if cur == n*2:
            self.res.append(res)
            return
        else:
            if c < n:
                cres = deepcopy(res)
                self.generateParenthesis_(c+1, cur+1, n, cres+"(")
                cres = deepcopy(res)
                self.generateParenthesis_(c, cur+1, n, cres+")")
            else:
                cres = deepcopy(res)
                self.generateParenthesis_(c, cur+1, n, cres+")")
            return


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.generateParenthesis_(0, 0, n, "")
        return self.res

        
