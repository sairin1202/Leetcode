"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        hash_map_real = {}
        hash_map_copy = {}
        cur = head
        hash_map_real[head] = 0
        copy_head = Node(cur.val, None, None)
        copy_cur = copy_head
        hash_map_copy[0] = copy_cur
        i = 0
        while cur.next:
            i += 1
            cur = cur.next
            copy_next = Node(cur.val, None, None)
            copy_cur.next = copy_next
            hash_map_real[cur] = i
            hash_map_copy[i] = copy_next
            copy_cur = copy_cur.next

        cur = head
        copy_cur = copy_head
        if cur.random:
            copy_cur.random = hash_map_copy[hash_map_real[cur.random]]
        while cur.next:
            cur = cur.next
            copy_cur = copy_cur.next
            if cur.random:
                copy_cur.random = hash_map_copy[hash_map_real[cur.random]]
        return copy_head
            
