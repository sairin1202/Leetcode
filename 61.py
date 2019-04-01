# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        cur = head
        length = 0
        while cur :
            cur = cur.next
            length += 1
        k = k % length
        if k == 0:
            return head

        cur = head
        times = length - k - 1
        while times > 0:
            cur = cur.next
            times-= 1
        cur_head = cur.next
        cur.next = None

        cur = cur_head
        while cur.next:
            cur = cur.next
        cur.next = head
        return cur_head
        
