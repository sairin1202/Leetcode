class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        c = 0
        res = ""
        if len(a) - len(b) > 0:
            b = "0"*(len(a) - len(b)) + b
        if len(b) - len(a) > 0:
            a = "0"*(len(b) - len(a)) + a
        idx = len(a)-1
        while idx >= 0 and idx >= 0:
            num_a = int(a[idx])
            num_b = int(b[idx])
            res = str((num_a+num_b+c)%2)+res
            c = (num_a+num_b+c)//2
            idx -= 1

        if c > 0:
            res = "1" + res

        return res
        
