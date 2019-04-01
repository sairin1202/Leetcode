from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # if t == "" or s == "":
        #     return ""
        # queue = []
        # dic = Counter(t)
        # # print(dic)
        # min_ = 1000000
        # res = ""
        # for idx, c in enumerate(s):
        #     if c in dic:
        #         if len(queue) < len(t):
        #             if dic[c] > 0:
        #                 dic[c] -= 1
        #                 queue.append((c,idx))
        #                 if len(queue) == len(t):
        #                     min_ = queue[-1][1] - queue[0][1]
        #                     res = s[queue[0][1]:queue[-1][1]+1]
        #             else:
        #                 # find c and change idx
        #                 for i in range(len(queue)):
        #                     if queue[i][0] == c:
        #                         queue.pop(i)
        #                         queue.append((c, idx))
        #                         break
        #         else:
        #             if c == queue[0][0]:
        #                 queue.pop(0)
        #                 queue.append((c, idx))
        #                 if min_ > queue[-1][1] - queue[0][1]:
        #                     min_ = queue[-1][1] - queue[0][1]
        #                     res = s[queue[0][1]:queue[-1][1]+1]
        #             else:
        #                 # find c and change idx
        #                 for i in range(len(queue)):
        #                     if queue[i][0] == c:
        #                         queue.pop(i)
        #                         queue.append((c, idx))
        #                         break
        # return res

        if t == "" or s == "":
            return ""
        dic = Counter(t)
        formed = 0
        required = len(dic)
        right = 0
        left = 0
        window = {}
        ans = [float("inf"), None, None]
        while right < len(s):
            c = s[right]
            if c in dic:
                # print(window)
                window[c] = window.get(c,0)+1
                if window[c] == dic[c]:
                    formed += 1

                while formed == required and left <= right:
                    if ans[0] > right - left:
                        ans = right-left, left, right
                    char = s[left]
                    if char in dic:
                        window[char] = window[char] - 1
                        if window[char] < dic[char]:
                            formed -= 1
                    left += 1

            right += 1
        if ans[1] == None:
            return ""
        return s[ans[1]:ans[2]+1]











        
