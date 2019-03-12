class Solution(object):

    def isPalindrome_(self, x, left, right):
        if left > right:
            return True
        if self.isPalindrome_(x, left+1, right-1):
            if x[left] == x[right]:
                return True
            else:
                return False
        else:
            return False

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return self.isPalindrome_(x, 0, len(x)-1)
