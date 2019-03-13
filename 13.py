class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        res = ""
        idx = 0
        while 1:
            if idx >= len(strs[0]):
                return res
            cur_c = strs[0][idx]
            for word in strs:
                if idx >= len(word):
                    return res
                if word[idx] != cur_c:
                    return res
            res += cur_c
            idx += 1
