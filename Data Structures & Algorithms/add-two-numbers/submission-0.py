# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        newList = dummy
        
        mem = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = mem + val1 + val2 

            newVal = total % 10
            newList.next = ListNode(newVal)

            mem = total // 10

            newList = newList.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if mem != 0:
            newList.next = ListNode(mem)
        
        return dummy.next