# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        cur_left = head
        cur_right = head.next
        cur_left.next = None
        while cur_right:
            target = cur_right
            cur_right = cur_right.next
            cur_left_copy = cur_left
            if cur_left_copy.val > target.val:
                target.next = cur_left_copy
                cur_left = target
            else:
                pre = cur_left_copy
                while cur_left_copy and target.val > cur_left_copy.val:
                    pre = cur_left_copy
                    cur_left_copy = cur_left_copy.next
                target.next = pre.next
                pre.next = target
        return cur_left
