class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainStack = []
        self.auxStack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.mainStack.append(x)
        if len(self.auxStack) == 0:
            self.auxStack.append(x)
        else:
            if self.auxStack[-1] >= x:
                self.auxStack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        num = self.mainStack.pop()
        if len(self.auxStack) and self.auxStack[-1] == num:
            self.auxStack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.mainStack):
            return self.mainStack[-1]
        else:
            return -1


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.auxStack):
            return self.auxStack[-1]
        else:
            return -1



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
