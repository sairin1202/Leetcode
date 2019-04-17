# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.inorder(root)
        for i in range(1, len(self.res)):
            if self.res[i] <= self.res[i-1]:
                return False
        return True
        
