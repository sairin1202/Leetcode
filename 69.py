class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left <= right:
            mid = (left+right)//2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                right = mid - 1
            if mid*mid < x:
                left = mid + 1
        return left - 1
        
