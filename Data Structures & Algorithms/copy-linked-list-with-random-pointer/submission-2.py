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

        cur = head
        while cur:
            tmp = cur.next
            cur.next = Node(cur.val, tmp)
            cur = tmp
        
        cur = head
        while cur:
            if cur.random != None:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head.next
        newList = cur
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            cur = tmp.next

        return newList
            

        
