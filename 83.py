# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            if cur.next == None:
                return head
            cur2 = cur.next
            while cur2 and cur2.val == cur.val:
                cur2 = cur2.next
            cur.next = cur2
            cur = cur.next
        return head
        
