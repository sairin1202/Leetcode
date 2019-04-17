# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def help(self, root):
        if not root:
            return 0
        return max(self.help(root.left), self.help(root.right))+1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.help(root)

        
