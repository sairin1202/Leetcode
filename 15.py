class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # O(n^3)
        # res = set()
        # for i in range(len(nums)):
        #     cur_1 = nums[i]
        #     for j in range(i+1,len(nums)):
        #         cur_2 = nums[j]
        #         for k in range(j+1,len(nums)):
        #             cur_3 = nums[k]
        #             if cur_1 + cur_2 + cur_3 == 0:
        #                 if cur_1 <= cur_2 and cur_1 <= cur_3:
        #                     if cur_2 < cur_3:
        #                         res.add((cur_1, cur_2, cur_3))
        #                     else:
        #                         res.add((cur_1, cur_3, cur_2))
        #                 if cur_2 <= cur_3 and cur_2 <= cur_1:
        #                     if cur_1 < cur_3:
        #                         res.add((cur_2, cur_1, cur_3))
        #                     else:
        #                         res.add((cur_2, cur_3, cur_1))
        #                 if cur_3 <= cur_1 and cur_3 <= cur_2:
        #                     if cur_2 < cur_1:
        #                         res.add((cur_3, cur_2, cur_1))
        #                     else:
        #                         res.add((cur_3, cur_1, cur_2))
        # return list(res)

#         O(n^2)
#         hash_table = {}
#         for i in range(len(nums)):
#             hash_table[nums[i]] = i

#         res = set()
#         for i in range(len(nums)):
#             cur_1 = nums[i]
#             for j in range(i+1,len(nums)):
#                 cur_2 = nums[j]
#                 if -1*cur_2-1*cur_1 in hash_table:
#                     if hash_table[-1*cur_2-1*cur_1] != i  and hash_table[-1*cur_2-1*cur_1] != j:
#                         cur_3 = -1*cur_2-1*cur_1
#                         if cur_1 <= cur_2 and cur_1 <= cur_3:
#                             if cur_2 < cur_3:
#                                 res.add((cur_1, cur_2, cur_3))
#                             else:
#                                 res.add((cur_1, cur_3, cur_2))
#                         if cur_2 <= cur_3 and cur_2 <= cur_1:
#                             if cur_1 < cur_3:
#                                 res.add((cur_2, cur_1, cur_3))
#                             else:
#                                 res.add((cur_2, cur_3, cur_1))
#                         if cur_3 <= cur_1 and cur_3 <= cur_2:
#                             if cur_2 < cur_1:
#                                 res.add((cur_3, cur_2, cur_1))
#                             else:
#                                 res.add((cur_3, cur_1, cur_2))
#         return list(res)

        nums.sort()
        res = set()
        for i, num  in enumerate(nums):
            start = i+1
            end = len(nums)-1
            while(start < end):
                if num + nums[start] + nums[end] > 0:
                    end -= 1
                elif num + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    res.add((num,nums[start],nums[end]))
                    start += 1
                    end -= 1
        return list(res)
                
