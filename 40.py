from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.res = []

#     def solve_(self, idx, candidates, target, cur_sum, cur_seq):
#         # print(idx)
#         print(cur_seq)
#         if cur_sum == target:
#             cur_seq_c = deepcopy(cur_seq)
#             self.res.append(cur_seq_c)
#         if idx == len(candidates):
#             return
#         if cur_sum > target:
#             return
#         else:
#             self.solve_(idx+1, candidates, target, cur_sum, cur_seq)
#             cur_sum += candidates[idx]
#             cur_seq.append(candidates[idx])
#             self.solve_(idx+1, candidates, target, cur_sum, cur_seq)
#             cur_seq.pop()
#         return

#     def combinationSum2(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         self.solve_(0, candidates, target, 0, [])
#         res = set()
#         for a in self.res:
#             a.sort()
#             res.add(tuple(a))
#         return res

    def solve(self, idx, candidates, target, cur_sum, cur_seq):
        # print(cur_sum,cur_seq)
        if cur_sum == target:
            cur_seq_c = deepcopy(cur_seq)
            self.res.append(cur_seq_c)
        if idx == len(candidates):
            return
        if cur_sum > target:
            return
        for i in range(idx, len(candidates)):
            # i > idx !!!
            if i>idx and candidates[i] == candidates[i-1]:
                continue
            cur_seq.append(candidates[i])
            cur_sum += candidates[i]
            self.solve(i+1, candidates, target, cur_sum, cur_seq)
            cur_seq.pop()
            cur_sum -= candidates[i]
        return

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.solve(0, candidates, target, 0, [])
        return self.res
