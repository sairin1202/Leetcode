class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for i in range(n-1):
            str_n = res
            cur = str_n[0]
            count = 1
            res = ""
            for j in range(1, len(str_n)):
                if str_n[j] == cur:
                    count += 1
                else:
                    res += str(count)+cur
                    cur = str_n[j]
                    count = 1
            res += str(count)+cur
        return res
        
