class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
#         # Solution 1
#         # dp solution
#         #   b a b a d
#         # b 1 0 1 0 0
#         # a   1 0 1 0
#         # b     1 0 0
#         # a       1 0
#         # d         1
#         max_len = 0
#         max_idx = (0,0)
#         dp = [[0]*len(s) for _ in range(len(s))]

#         for i in range(len(s)):
#             for j in range(i+1):
#                 dp[i][j] = 1

#         for j in range(len(s)-2,-1,-1):
#             for i in range(j+1,len(s)):
#                 if s[j] == s[i]:

#                     if dp[j+1][i-1] == 1:
#                         dp[j][i] = 1
#                         if i-j > max_len:
#                             max_len = i-j
#                             max_idx = (j,i)
#         return s[max_idx[0]:max_idx[1]+1]

#         Solution 2
#         Manacher Algorithm
#             # b # a # b # a # d #
#         len 0 1 0 3 0 3 .........
#             # b # a # b #
#            left       right
#         when calculate second b, first b is lower bound <= a's lower bound
#         len(b) = min(len(first b)) continue checking left and right
#         else if first b is lower bound > a's lower bound
#         len(b) = len(fisrt b)

        # insert # into the s
        new_s = [" "]* (len(s)*2+1)
        for i in range(len(new_s)):
            new_s[i] = "#" if i%2 == 0 else s[i//2]

        radio = [0] * len(new_s)
        left = -1
        right = -1
        lagest_radio_idx = -1
        max_ = (-1,-1)
        for i, char in enumerate(new_s):
            if i >= right:
                len_ = 0
                while (i-len_-1>=0 and i+len_+1<len(new_s)) and new_s[i-len_-1] == new_s[i+len_+1]:
                    len_ += 1

            if i < right:
                if i-2*(i-largest_radio_idx) - radio[i-2*(i-largest_radio_idx)] > left:
                    len_ = radio[i-2*(i-largest_radio_idx)]
                else:
                    len_ = i-2*(i-largest_radio_idx) - left
                    while (i-len_-1>=0 and i+len_+1<len(new_s)) and new_s[i-len_-1] == new_s[i+len_+1]:
                        len_ += 1

            if i + len_ > right:
                right = i + len_
                left = i - len_
                largest_radio_idx = i

            radio[i] = len_
            if len_ > max_[1]:
                max_ = (i, len_)

        if max_[1] % 2 == 0:
            return s[max_[0]//2-max_[1]//2:max_[0]//2+max_[1]//2]
        else:
            return s[max_[0]//2-max_[1]//2:max_[0]//2+max_[1]//2+1]


            
