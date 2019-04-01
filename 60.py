class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        res = ""
        nums = [i+1 for i in range(9)]
        facts = []
        mul = 1
        for i in range(2,10):
            facts.append(mul)
            mul *= i
        # print(facts)
        for i in range(n-1):
            idx = k//facts[n-i-2]
            res += str(nums[idx])
            nums.pop(idx)
            k = k%facts[n-i-2]

            # print(k)
        res += str(nums[0])
        return res
            
