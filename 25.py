# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isEnd(self, c_head, k):
        curs = [c_head]
        if c_head == None:
            return True, curs
        for _ in range(k-1):
            c_head = c_head.next
            curs.append(c_head)
            if c_head == None:
                return True, curs
        return False, curs

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        new_head = ListNode(0)
        cur_head = new_head
        end, curs = self.isEnd(head, k)
        if end:
            return head
        cur_head.next = curs[-1]
        while 1:
            curs[0].next = curs[-1].next
            for i in range(1,len(curs)):
                curs[i].next = curs[i-1]
            tmp = curs[0]
            end, curs = self.isEnd(curs[0].next, k)
            if end:
                return new_head.next
            tmp.next = curs[-1]
