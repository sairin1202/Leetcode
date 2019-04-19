# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        stack = [[root, 0]]
        while stack:
            cur, sign = stack[-1]
            if sign == 1:
                cur, sign = stack.pop()
                res.append(cur.val)
                if cur.right:
                    stack.append([cur.right, 0])
                continue
            stack[-1][1] = 1
            if cur.left:
                stack.append([cur.left, 0])
                continue
        return res
                
