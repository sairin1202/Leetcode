class Solution(object):
#     def __init__(self):
#         self.count = 0

#     def numDecodings_(self, s, idx):
#         if idx == len(s):
#             self.count += 1
#             return
#         if idx + 2 <= len(s):
#             if s[idx] != '0' and 1<= int(s[idx:idx+2]) <= 26:
#                 self.numDecodings_(s, idx+2)
#         if s[idx] != '0':
#             self.numDecodings_(s, idx+1)

#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         self.numDecodings_(s, 0)
#         return self.count


    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        nums = [0]*(len(s)+1)
        nums[1] = 1
        nums[0] = 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if not "1" <= s[i-1] <= "2":
                    return 0
                else:
                    nums[i+1] = nums[i-2+1]
            elif s[i] <= "6":
                if "1" <= s[i-1] <= "2":
                    nums[i+1] = nums[i-1+1] + nums[i-2+1]
                else:
                    nums[i+1] = nums[i-1+1]
            else:
                if s[i-1] == "1":
                    nums[i+1] = nums[i-1+1] + nums[i-2+1]
                else:
                    nums[i+1] = nums[i-1+1]
        # print(nums)
        return nums[-1]



            
