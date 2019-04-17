# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.first = None
        self.second = None
        self.pre = None
        self.root = None
        self.start = False

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            if self.start:
                if root.val < self.pre.val:
                    if self.first == None:
                        self.first = self.pre
                        self.second = root
                    else:
                        self.second = root

            self.pre = root
            self.start = True
            self.inorder(root.right)


    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.root = root
        self.inorder(root)
        self.second.val, self.first.val = self.first.val, self.second.val
        
