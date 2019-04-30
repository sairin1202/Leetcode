# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if root == None:
            return root
        if root.left == None:
            root.right = None
            return root
        self.dfs(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None
        return root


    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        new_root = root
        while new_root.left:
            new_root = new_root.left
        self.dfs(root)
        return new_root
        
