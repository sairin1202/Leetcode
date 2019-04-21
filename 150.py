class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t == "+":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t1+t2)
            elif t == "-":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2-t1)
            elif t == "*":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t1*t2)
            elif t == "/":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(int(float(t2)/t1))
            else:
                t = int(t)
                stack.append(t)
        return stack[-1]
