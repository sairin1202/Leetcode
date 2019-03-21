from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.res = []


    def comb_(self, candidates, idx, target, cur_sum, cur_seq):
        if idx >= len(candidates):
            return
        cur_seq_copy = deepcopy(cur_seq)
        # take candidates[idx]
        if cur_sum + candidates[idx] <= target:
            next_sum = cur_sum + candidates[idx]
            cur_seq_new = deepcopy(cur_seq_copy)
            cur_seq_new.append(candidates[idx])
            if next_sum == target:
                self.res.append(cur_seq_new)
            else:
                self.comb_(candidates, idx, target, next_sum, cur_seq_new)
        # not take candidates[idx]
        self.comb_(candidates, idx+1, target, cur_sum, cur_seq_copy)
        return


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.comb_(candidates, 0, target, 0, [])
        return self.res
        
