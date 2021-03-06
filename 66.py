class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c = 1
        for i in range(len(digits)-1, -1, -1):
            temp = digits[i]
            digits[i]  = (digits[i] + c)%10
            c = (temp + 1)//10
            if c == 0:
                break
        if c == 1:
            digits.insert(0,1)
        return digits
