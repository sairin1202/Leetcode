# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        cur_head = new_head
        cur1 = head
        if cur1 == None:
            return head
        cur2 = head.next
        if cur2 == None:
            return head

        while 1:
            cur_head.next = cur2
            cur1.next = cur2.next
            cur2.next = cur1
            cur_head = cur1
            if cur_head.next == None or cur_head.next.next == None:
                return new_head.next
            else:
                cur1 = cur_head.next
                cur2 = cur_head.next.next
        
