# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, head):
        if head == None:
            return None
        # print(head.val)
        first = head
        second = head
        pre = first
        node = None
        while second.next and second.next.next:
            pre = first
            first = first.next
            second = second.next.next
        node = TreeNode(first.val)
        node.right = self.helper(first.next)
        if pre != first:
            pre.next = None
        else:
            head = None
        node.left = self.helper(head)
        return node


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.helper(head)

        
