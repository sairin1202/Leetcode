class Solution(object):
    def myPow_(self, x, n):
        if n == 1:
            return x
        if n % 2 == 0:
            return self.myPow_(x, n//2)**2
        else:
            return self.myPow_(x, n//2)**2 * x

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1.0/x
        # print(x,n)
        if n == 0:
            return 1
        return self.myPow_(x, n)

        
