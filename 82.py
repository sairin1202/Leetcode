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
        res_head = None

        while cur:
            count = 1
            while cur.next and cur.next.val == cur.val:
                count += 1
                cur = cur.next
            if count == 1:
                if res_head == None:
                    res_head = ListNode(cur.val)
                    res_cur = res_head
                else:
                    res_cur.next = ListNode(cur.val)
                    res_cur = res_cur.next
            cur = cur.next

        return res_head

        
