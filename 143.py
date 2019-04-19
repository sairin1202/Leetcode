# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        left = 0
        right = len(nodes) - 1
        control = 0
        while left < right:
            if control == 0:
                cur = nodes[left]
                next_cur = nodes[right]
                cur.next = next_cur
                left += 1
                control ^= 1
            else:
                cur = nodes[right]
                next_cur = nodes[left]
                cur.next = next_cur
                right -= 1
                control ^= 1
        nodes[left].next = None
        return nodes[0]
            
