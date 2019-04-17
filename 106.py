# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.index = 0

    def helper(self, postorder, inorder, left, right):
        if left > right:
            return None
        if self.index == len(postorder):
            return None
        node = None
        for i in range(right, left-1, -1):
            if inorder[i] == postorder[len(postorder)-self.index-1]:
                node = TreeNode(postorder[len(postorder)-self.index-1])
                self.index += 1
                node.right = self.helper(postorder, inorder, i+1, right)
                node.left = self.helper(postorder, inorder, left, i-1)
                break
        return node

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(postorder, inorder, 0, len(postorder)-1)
        
