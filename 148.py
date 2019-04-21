# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, left, right):
        if left.val < right.val:
            head = ListNode(left.val)
            left = left.next
        else:
            head = ListNode(right.val)
            right = right.next
        cur = head
        while left and right:
            if left.val < right.val:
                cur.next = ListNode(left.val)
                left = left.next
            else:
                cur.next = ListNode(right.val)
                right = right.next
            cur = cur.next
        while left:
            cur.next = ListNode(left.val)
            left = left.next
            cur = cur.next
        while right:
            cur.next = ListNode(right.val)
            right = right.next
            cur = cur.next

        return head


    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next
        slow.next = None
        lhead = self.mergeSort(left)
        rhead = self.mergeSort(right)
        head = self.merge(lhead, rhead)
        return head




    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)
        
