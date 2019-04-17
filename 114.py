# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
#     sorted flatten
#     def helper(self, root):
#         if root == None:
#             return None
#         if root.left == None and root.right == None:
#             return root
#         if root.left == None or root.right == None:
#             if root.left == None:
#                 root.right = self.helper(root.right)
#             if root.right == None:
#                 root.right = self.helper(root.left)
#                 root.left = None
#             cur = root
#             while cur.right and cur.right.val < cur.val:
#                 cur.right.val, cur.val = cur.val, cur.right.val
#                 cur = cur.right
#             return root
#         else:
#             left = self.helper(root.left)
#             right = self.helper(root.right)
#             if left.val < right.val:
#                 root.right = left
#                 root.left = right
#             else:
#                 root.right = right
#                 root.left = left
#             cur = root
#             while cur.right and cur.right.val < cur.val:
#                 cur.right.val, cur.val = cur.val, cur.right.val
#                 cur = cur.right

#             cur = root
#             left_cur = root.left
#             root.left = None
#             while left_cur:
#                 temp = left_cur
#                 left_cur = left_cur.right
#                 while cur.right and cur.right.val < temp.val:
#                     cur = cur.right
#                 temp.right = cur.right
#                 cur.right = temp
#                 cur = cur.right
#             return root

    def helper(self, root):
        if root == None:
            return None,None
        if root.left == None and root.right == None:
            return root, root
        if root.left == None:
            low, high = self.helper(root.right)
            return low, root
        if root.right == None:
            low, high= self.helper(root.left)
            root.right = high
            root.left = None
            return low, root
        left_low, left_high = self.helper(root.left)
        right_low, right_high = self.helper(root.right)
        root.right = left_high
        left_low.right = right_high
        root.left = None
        return right_low, root




    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        low, high = self.helper(root)
        return high
        
