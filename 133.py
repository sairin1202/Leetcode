"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        nodeSet = {}
        newNode = Node(node.val, [])
        queue = [(node, newNode)]
        nodeSet[node] = newNode
        head = None
        while len(queue):
            real, copy = queue.pop(0)
            if head == None:
                head = newNode
            for n in real.neighbors:
                if n in nodeSet:
                    copy.neighbors.append(nodeSet[n])
                    continue
                newChild = Node(n.val ,[])
                copy.neighbors.append(newChild)
                queue.append((n, newChild))
                nodeSet[n] = newChild
        return head
