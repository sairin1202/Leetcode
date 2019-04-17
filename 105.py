# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.index = 0

    def help(self, preorders, idx, inorders, left, right):
        if idx == len(preorders):
            return None
        if left > right:
            return None
        node = None
        # print(left, right, preorders[idx])
        for i in range(left, right+1):
            if preorders[idx] == inorders[i]:
                self.index += 1
                node = TreeNode(preorders[idx])
                break
        if node == None:
            return None
        node.left = self.help(preorders, self.index, inorders, left, i-1)
        if node.left == None:
            node.right = self.help(preorders, self.index, inorders, i+1, right)
        else:
            node.right = self.help(preorders, self.index, inorders, i+1, right)
        return node




    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.help(preorder, self.index, inorder, 0, len(preorder)-1)

        
