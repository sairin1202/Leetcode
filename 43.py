class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum_ = 0
        for i, n2 in enumerate(num2[::-1]):
            c = 0
            for j, n1 in enumerate(num1[::-1]):
                ni1 = ord(n1) - ord('0')
                ni2 = ord(n2) - ord('0')
                n = ni1 * ni2 + c
                c = n // 10
                sum_ += n % 10 * (10**(j+i))
            if c > 0:
                 sum_ += c * (10**(j+i+1))
        return str(sum_)
            
