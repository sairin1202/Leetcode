class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0:
            return -1
        idx = -1
        if gas[0] - cost[0] < 0:
            stack = [gas[0]- cost[0]]
        else:
            idx = 0
            stack = [gas[0]- cost[0]]
        for i in range(1, len(gas)):
            num = gas[i] - cost[i]
            if num <= 0:
                if stack[-1] < 0:
                    stack.append(num)
                else:
                    stack[-1] += num
                    if stack[-1] < 0:
                        idx = -1
            else:
                if stack[-1] > 0:
                    stack[-1] += num
                else:
                    stack.append(num)
                    idx = i
            # print(idx)
            # print(stack)
        if sum(stack) >= 0:
            return idx
        else:
            return -1

        
