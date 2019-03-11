# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def addTwoCells(self, l1, l2, c):
        if l1 == None and l2 == None:
            if c == 0:
                return None
            else:
                new_node = ListNode(1)
                return new_node

        elif l1 == None:
            val = (l2.val + c) % 10
            c = (l2.val + c) // 10
            new_node = ListNode(val)
            new_node.next = self.addTwoCells(l1, l2.next, c)

        elif l2 == None:
            val = (l1.val + c) % 10
            c = (l1.val + c) // 10
            new_node = ListNode(val)
            new_node.next = self.addTwoCells(l1.next, l2, c)

        else:
            val = (l1.val + l2.val + c) % 10
            c = (l1.val + l2.val + c) // 10
            new_node = ListNode(val)
            new_node.next = self.addTwoCells(l1.next, l2.next, c)

        return new_node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        res = self.addTwoCells(l1, l2, c)
        return res