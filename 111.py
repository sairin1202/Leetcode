# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == 0:
            return right+1
        if right == 0:
            return left+1
        return min(left, right)+1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)
