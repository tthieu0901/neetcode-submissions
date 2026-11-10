# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def count(head):
            if head == None: return 0
            return 1 + count(head.next)
        
        prev = None
        cur = head

        pos = count(head) - n
        
        if pos == 0:
            return head.next
        
        if pos < 0:
            return None
        
        while cur and pos > 0:
            pos -= 1
            prev = cur
            cur = cur.next

        prev.next = cur.next
        return head