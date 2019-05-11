class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return ["{}->{}".format(lower, upper)]
        res = []
        cur = lower
        for num in nums:
            if num > cur:
                if num - 1 == cur:
                    res.append(str(cur))
                else:
                    res.append("{}->{}".format(cur, num-1))
            cur = num + 1
        if upper >= cur:
            if upper == cur:
                res.append(str(upper))
            else:
                res.append("{}->{}".format(cur, upper))
        return res
