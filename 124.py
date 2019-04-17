# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = float("-inf")


    def helper(self, root):
        if root == None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        left_t = 0 if left < 0 else left
        right_t = 0 if right < 0 else right
        if root.val + left_t + right_t > self.res:
            self.res = root.val + left_t + right_t

        return max(left_t, right_t)+ root.val


    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.res
        
