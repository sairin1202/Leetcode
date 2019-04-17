# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []

    def dfs(self, root, res):
        if root.left == None and root.right == None:
            res.append(root.val)
            self.res.append(res[::-1])
            res.pop()
            return
        res.append(root.val)
        if root.left:
            self.dfs(root.left, res)
        if root.right:
            self.dfs(root.right, res)
        res.pop()
        return


    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.dfs(root,[])
        # print(self.res)
        sum_ = 0
        for res in self.res:
            num = 0
            for i in range(len(res)):
                num += res[i]*(10**i)
            sum_ += num
        return sum_
        
