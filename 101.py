# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.post1 = []
        self.post2 = []

    def postorder1(self, root):
        if root:
            self.postorder1(root.left)
            self.postorder1(root.right)
            self.post1.append(root.val)
        else:
            self.post1.append(0)

    def postorder2(self, root):
        if root:
            self.postorder2(root.right)
            self.postorder2(root.left)
            self.post2.append(root.val)
        else:
            self.post2.append(0)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        self.postorder1(root.left)
        self.postorder2(root.right)
        self.post1 = tuple(self.post1)
        self.post2 = tuple(self.post2)
        # print(self.post1)
        # print(self.post2)
        return True if self.post1 == self.post2 else False



            
