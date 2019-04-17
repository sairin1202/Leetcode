# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def generateTrees_(self, left, right):
        if left >= right:
            return [None]
        res = []
        for m in range(left, right):
            left_res = self.generateTrees_(left, m)
            right_res = self.generateTrees_(m+1, right)
            for l in left_res:
                for r in right_res:
                    current = TreeNode(m)
                    current.left = l
                    current.right = r
                    res.append(current)

        return res



    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generateTrees_(1, n+1)
        
