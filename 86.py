# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return head
        less_head = ListNode(-1)

        cur = head
        less_cur = less_head
        while cur and cur.val < x:
            less_cur.next = cur
            less_cur = less_cur.next
            cur = cur.next
        head = cur
        if head == None:
            return less_head.next

        while cur.next:
            if cur.next.val < x:
                less_cur.next = cur.next
                cur.next = cur.next.next
                less_cur = less_cur.next
                # print(cur.next)
                # print(less_cur.val)
            else:
                cur = cur.next
            if cur == None:
                break

        less_cur.next = head
        return less_head.next
