"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        p = head
        self.nodes = {}
        while p:
            self.nodes[p] = Node(p.val)
            p = p.next

        p = head
        while p:
            newNode = self.nodes[p]
            if p.next: 
                newNode.next = self.nodes[p.next]
            if p.random:
                newNode.random = self.nodes[p.random]
            p = p.next

        return self.nodes[head] 

        
