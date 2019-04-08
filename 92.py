# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        length = n-m
        new_node = ListNode(-1)
        new_node.next = head
        head = new_node
        cur = head
        while cur and m-1 > 0:
            m -= 1
            cur = cur.next

        if cur == None:
            return head
        if cur.next == None:
            return head

        temp = cur.next
        new_head = cur.next
        pre = new_head
        pro = pre.next

        while length+1 > 0:
            length -= 1
            pre.next = new_head
            new_head = pre
            pre = pro
            if pro:
                pro = pro.next
            # print(new_head.val)
        cur.next = new_head
        temp.next = pre
        return head.next

        
