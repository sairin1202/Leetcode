# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        queue = [(root,0)]
        level_res = []
        cur_level = 0
        while len(queue):
            cur, level = queue.pop(0)
            if level != cur_level:
                res.append(level_res[:])
                cur_level = level
                level_res = [cur.val]
            else:
                level_res.append(cur.val)
            if cur.left:
                queue.append((cur.left, level+1))
            if cur.right:
                queue.append((cur.right, level+1))
        res.append(level_res)
        return res
            
