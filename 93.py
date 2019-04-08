class Solution(object):
    def __init__(self):
        self.res = []

    def help(self, s, idx, res):
        if len(res) > 4:
            return
        if idx >= len(s):
            if len(res) == 4:
                self.res.append(res[:])
                return
            else:
                return
        if s[idx] == "0":
            res.append(s[idx:idx+1])
            self.help(s, idx+1, res)
            res.pop()
        else:
            if idx+2 <= len(s):
                res.append(s[idx:idx+2])
                self.help(s, idx+2, res)
                res.pop()
            res.append(s[idx:idx+1])
            self.help(s, idx+1, res)
            res.pop()
            if idx+3 <= len(s):
                if 100 <= int(s[idx:idx+3]) <= 255:
                    res.append(s[idx:idx+3])
                    self.help(s, idx+3, res)
                    res.pop()


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.help(s, 0, res)
        # print(self.res)
        return [".".join(res) for res in self.res]
