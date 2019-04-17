# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if not root:
            return 0, True
        left, res_l = self.helper(root.left)
        right, res_r = self.helper(root.right)
        if res_l == False or res_r == False:
            return max(left, right)+1, False
        if abs(left - right) > 1:
            return max(left, right)+1, False
        return max(left, right)+1, True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height, res = self.helper(root)
        return res
