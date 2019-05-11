# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.array = []
        self.inorder(root)
        self.index = 0

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.array.append(root.val)
            self.inorder(root.right)


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        res = self.array[self.index]
        self.index += 1
        return res


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.index >= len(self.array):
            return False
        return True




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
