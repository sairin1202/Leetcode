# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        follow = head
        ahead = head
        for _ in range(n):
            if ahead == None:
                return []
            ahead = ahead.next

        if ahead == None:
            return head.next

        while ahead.next:
            follow = follow.next
            ahead = ahead.next

        follow.next = follow.next.next
        return head
