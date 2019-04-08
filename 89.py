class Solution(object):
    def __init__(self):
        self.res = [0, 1]


    def grayCode_(self, n, count, cur, cur_num, nums, res):
        if count == 2**n:
            return True
        for i in range(n):
            if cur[i] == 0:
                cur_num += 2**i
                if nums[cur_num]:
                    cur_num -= 2**i
                    continue
                cur[i] = 1
                nums[cur_num] = 1
                res.append(cur_num)
                if self.grayCode_(n, count+1, cur, cur_num, nums, res):
                    return True
                cur_num -= 2**i
                cur[i] = 0
                nums[cur_num] = 0
                res.pop()
            else:
                cur_num -= 2**i
                if nums[cur_num]:
                    cur_num += 2**i
                    continue
                cur[i] = 0
                nums[cur_num] = 1
                res.append(cur_num)
                if self.grayCode_(n, count+1, cur, cur_num, nums, res):
                    return True
                cur_num += 2**i
                cur[i] = 1
                nums[cur_num] = 0
                res.pop()
        return False


    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        nums = [0]*(2**n)
        nums[0] = 1
        nums[1] = 1
        cur = [0]*n
        cur[0] = 1
        count = 2
        res = [0,1]
        self.grayCode_(n, count, cur, 1, nums, res)
        return res
