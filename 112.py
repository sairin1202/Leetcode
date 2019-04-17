# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, res, sum):
        if not root:
            return False
        if root.left == None and root.right == None:
            if res+root.val == sum:
                return True
            else:
                return False
        if self.dfs(root.left, res+root.val, sum) or self.dfs(root.right, res+root.val, sum):
            return True
        return False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        return self.dfs(root, 0, sum)
