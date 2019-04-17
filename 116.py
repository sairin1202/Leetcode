"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return root
        queue = [(root, 0)]
        cur_level = -1
        while len(queue):
            cur, level = queue.pop(0)
            if level == cur_level:
                pre.next = cur
                pre = cur
            else:
                cur_level = level
                pre = cur
            if cur.left:
                queue.append((cur.left, level+1))
            if cur.right:
                queue.append((cur.right, level+1))

        return root
