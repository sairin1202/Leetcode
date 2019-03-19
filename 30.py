from copy import deepcopy
class Solution(object):

#     def slideWindow(self, s, word_len):
#         words = []
#         idx = 0
#         while idx + word_len <= len(s):
#             words.append(s[idx:idx+word_len])
#             idx += word_len
#         return words

#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         res = []
#         word_hash_map = {}
#         for i, word in enumerate(words):
#             if word not in word_hash_map:
#                 word_hash_map[word] = [i]
#             else:
#                 word_hash_map[word].append(i)
#         if len(words) == 0:
#             return []
#         word_len = len(words[0])
#         for i in range(word_len):
#             string = self.slideWindow(s[i:], word_len)

#             j = 0
#             while j < len(string)+1-len(words):
#                 substring = string[j:j+len(words)]
#                 hash_map = deepcopy(word_hash_map)
#                 appearance = [0]*len(words)
#                 # record whether each word has appearance
#                 count_hash_map = {}
#                 # print(i+j*word_len)
#                 # print(substring)
#                 for m, word in enumerate(substring):
#                     if word in hash_map:
#                         if word not in hash_map:
#                             j += m
#                             break
#                         if len(hash_map[word]) == 0:
#                             j = count_hash_map[word]
#                             break
#                         idx = hash_map[word].pop()
#                         if word not in count_hash_map:
#                             count_hash_map[word] = m + j
#                         appearance[idx] = 1
#                     else:
#                         break
#                 if sum(appearance) == len(words):
#                     res.append(i+j*word_len)
#                 j+=1
#         return res

    def slideWindow(self, s, word_len):
        words = []
        idx = 0
        while idx + word_len <= len(s):
            words.append(s[idx:idx+word_len])
            idx += word_len
        return words

    def isValid(self, s , word_hash_map, word_len, word_num):
        hash_map = deepcopy(word_hash_map)
        checkwords = self.slideWindow(s, word_len)
        appear = [0] * word_num
        for word in checkwords:
            if word not in hash_map:
                print(1)
                return False
            if len(hash_map[word]) == 0:
                print(2)
                return False
            else:
                hash_map[word].pop()
        return True


    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if len(words) == 0:
            return []

        res = []
        word_num = len(words)
        word_len = len(words[0])

        hash_map = {}
        for i, word in enumerate(words):
            if word not in hash_map:
                hash_map[word] = [i]
            else:
                hash_map[word].append(i)

        chash_map = {}
        for i, word in enumerate(words):
            for c in word:
                if c not in chash_map:
                    chash_map[c] = 1
                else:
                    chash_map[c] += 1

        count_hash_map = {}
        char_hash_map = deepcopy(chash_map)
        i = 0
        count = 0
        start = 0
        while i < len(s):
            c = s[i]
            if c not in chash_map:
                i += 1
                count = 0
                count_hash_map = {}
                char_hash_map = deepcopy(chash_map)
                start = i
            else:
                if char_hash_map[c] == 0:
                    count = i - count_hash_map[c][0]
                    for j in range(start, count_hash_map[c][0]):
                        char_hash_map[s[j]] += 1
                    start = count_hash_map[c][0] + 1
                    count_hash_map[c].append(i)
                    if len(count_hash_map[c]) > chash_map[c]:
                        count_hash_map[c].pop(0)
                    i += 1
                else:
                    char_hash_map[c] -= 1
                    if c not in count_hash_map:
                        count_hash_map[c] = [i]
                    else:
                        count_hash_map[c].append(i)
                    if len(count_hash_map[c]) > chash_map[c]:
                        count_hash_map[c].pop(0)
                    count += 1
                    i += 1
            # print(count_hash_map)
            # print(char_hash_map)
            # print(count)
            if count == word_num*word_len:
                # print(s[i-count:i])
                if self.isValid(s[i-count:i], hash_map, word_len, word_num):
                    res.append(i-count)
        return res




        
