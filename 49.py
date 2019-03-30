from copy import deepcopy
class Solution(object):

#     def test(self, word, dic):
#         word_dic = deepcopy(dic)
#         for c in word:
#             if c not in word_dic:
#                 return False
#             else:
#                 if word_dic[c] <= 0:
#                     return False
#                 else:
#                     word_dic[c] -= 1
#         for key, value in word_dic.items():
#             if word_dic[key] != 0:
#                 return False
#         return True

#     def createDic(self, word):
#         dic = {}
#         for c in word:
#             if c not in dic:
#                 dic[c] = 1
#             else:
#                 dic[c] += 1
#         return dic

    def createDic(self, word):
        dic = [0]*26
        for c in word:
            dic[ord(c)-ord("a")] += 1
        return tuple(dic)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        dicts = {}
        count = 0
        for word in strs:
            dic = self.createDic(word)
            if dic in dicts:
                res[dicts[dic]].append(word)
            else:
                dicts[dic] = count
                count += 1
                res.append([word])
        return res










        
