class Solution(object):
#     def calNext(self, s):
#         max_len = 0
#         for i in range(1, len(s)):
#             if s[:i] == s[-i:]:
#                 max_len = i
#         return max_len
    
#     def createNext(self, needle):
#         next = [0] * len(needle)
#         for i in range(len(needle)):
#             next[i] = self.calNext(needle[:i+1])
#         return next

    def createNext(self, needle):
        next = [-1] * len(needle)
        i = 0
        k = -1 # pre
        while i < len(needle)-1:
            if needle[k] == needle[i]:
                next[i+1] = k + 1
                i += 1
                k += 1
            else:
                k = next[k]
                if k == -1:
                    next[i+1] = 0
                    i += 1
                    k = 0
                
        return next
            
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        next = self.createNext(needle)
        h_idx = 0
        n_idx = 0
        while h_idx < len(haystack):     
            if haystack[h_idx] == needle[n_idx]:
                h_idx +=1
                n_idx +=1
                if n_idx >= len(needle):
                    return h_idx - len(needle)
            else:
                if next[n_idx] == -1:
                    n_idx = next[n_idx]
                    n_idx += 1
                    h_idx += 1
                else:
                    n_idx = next[n_idx]
        return -1
        
        
#         multiple answers
#         res = []
#         if needle == "":
#             return 0
#         next = self.createNext(needle)
#         next.insert(0, -1)
#         h_idx = 0
#         n_idx = 0
#         while h_idx < len(haystack):     
#             if haystack[h_idx] == needle[n_idx]:
#                 h_idx +=1
#                 n_idx +=1
#                 if n_idx >= len(needle):
#                     res.append(h_idx - len(needle))
#                     n_idx = next[n_idx]
#             else:
#                 if next[n_idx] == -1:
#                     n_idx = next[n_idx]
#                     n_idx += 1
#                     h_idx += 1
#                 else:
#                     n_idx = next[n_idx]
#         return res
                    
                    
                    
                    
        
