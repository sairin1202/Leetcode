# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempA = headA
        tempB = headB
        while headA != headB:
            if headA == None:
                headA = tempB
            else:
                headA = headA.next
            if headB == None:
                headB = tempA
            else:
                headB = headB.next
        return headA
            
