class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        hash_table = {s[0] : 1}
        count = 1
        left = 0
        right = 0
        res = float("-inf")
        while right < len(s):
            # print(hash_table)
            if count > 2:
                remove = s[left]
                left += 1
                hash_table[remove] -= 1
                if hash_table[remove] == 0:
                    count -= 1
            else:
                res = max(res, right-left+1)
                right += 1
                if right == len(s):
                    return res
                if s[right] not in hash_table or hash_table[s[right]] == 0:
                    hash_table[s[right]] = 1
                    count += 1
                else:
                    hash_table[s[right]] += 1
        return res
