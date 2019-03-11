class Solution(object):
    def check(self,x):
        lower_bound = -(2**31)
        upper_bound = (2**31)-1
        if x < lower_bound:
            return False
        if x > upper_bound:
            return False
        return True

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        x = str(x)
        idx = len(x) - 1
        while(x[idx] == '0'):
            idx -= 1
        if x[0] == "-":
            return int(x[idx:0:-1])*(-1) if self.check(int(x[idx:0:-1])*(-1)) else 0
        else:
            return int(x[idx::-1]) if self.check(int(x[idx::-1])) else 0
        
