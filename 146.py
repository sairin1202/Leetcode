class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None
    def show(self):
        return self.key, self.value, self.pre, self.next

class DLinkList(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.len = 0

    def printList(self):
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            print(cur.key, cur.value)

    def add(self, new_node):
        self.tail.pre.next = new_node
        new_node.pre = self.tail.pre
        self.tail.pre = new_node
        new_node.next = self.tail
        self.len += 1
        key = None
        node = None
        if self.len > self.capacity:
            key, node = self.delete()
        return key, node

    def delete(self):
        if self.len:
            key = self.head.next.key
            node = self.head.next
            self.head.next.next.pre = self.head
            self.head.next = self.head.next.next
            self.len -= 1
            return key, node
        return None, None

    def remove_to_end(self, node, value):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.len -= 1
        node = Node(node.key, value)
        self.add(node)
        return node


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dlinklist = DLinkList(capacity)
        self.hash_map = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_map or self.hash_map[key] == None:
            return -1
        else:
            node = self.hash_map[key]
            node = self.dlinklist.remove_to_end(node, node.value)
            self.hash_map[key] = node
        # print("-"*40)
        # self.dlinklist.printList()
        return node.value




    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.hash_map or self.hash_map[key] == None:
            node = Node(key, value)
            self.hash_map[key] = node
            key, node = self.dlinklist.add(node)
            self.hash_map[key] = None
        else:
            node = self.hash_map[key]
            node = self.dlinklist.remove_to_end(node, value)
            self.hash_map[key] = node
        # print("-"*40)
        # self.dlinklist.printList()




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
