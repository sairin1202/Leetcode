# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []

    def dfs(self, root, res, sum):
        if not root:
            return
        sum -= root.val
        res.append(root.val)
        if root.left == None and root.right == None:
            if sum == 0:
                self.res.append(res[:])
        elif root.left == None:
            self.dfs(root.right, res, sum)
        elif root.right == None:
            self.dfs(root.left, res, sum)
        else:
            self.dfs(root.left, res, sum)
            self.dfs(root.right, res, sum)
        res.pop()
        return


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.dfs(root, [], sum)
        return self.res
