class Solution(object):

    ##hashmap record index, current length, current start
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        cur_len = 0
        cur_start = 0
        hash_map = {}
        for i, char in enumerate(s):
            if char not in hash_map:
                hash_map[char] = i
                cur_len += 1
            else:
                if hash_map[char] >= cur_start:
                    max_len = cur_len if cur_len > max_len else max_len
                    cur_len = i - hash_map[char]
                    cur_start = hash_map[char] + 1
                    hash_map[char] = i
                else:
                    hash_map[char] = i
                    cur_len += 1
        max_len = cur_len if cur_len > max_len else max_len

        return max_len
