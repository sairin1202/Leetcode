# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from copy import deepcopy
class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        queue = []
        for l in lists:
            if l == None:
                continue
            idx = len(queue)-1
            while idx >= 0:
                if queue[idx].val > l.val:
                    idx -= 1
                else:
                    break
            queue.insert(idx+1, l)
        head = ListNode(-1)
        cur = head
        while len(queue):
            top = queue.pop(0)
            cur.next = top
            cur = cur.next
            top = top.next
            if top == None:
                continue
            idx = len(queue)-1
            while idx >= 0:
                if queue[idx].val > top.val:
                    idx -= 1
                else:
                    break
            queue.insert(idx+1, top)
        return head.next

        
