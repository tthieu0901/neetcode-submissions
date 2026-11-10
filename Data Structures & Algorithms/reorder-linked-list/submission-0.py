# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def half(self, head):
        if not head:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def reverse(self, head):
        if not head or not head.next:
            return head

        tail = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return tail

    def merge(self, list1, list2):
        dummy = ListNode()
        newList = dummy

        while list1 and list2:
            newList.next = list1
            newList = newList.next
            list1 = list1.next

            newList.next = list2
            newList = newList.next
            list2 = list2.next            

        if list1:
            newList.next = list1
        if list2:
            newList.next = list2

        return dummy.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        halfList = self.half(head)
        second = halfList.next
        halfList.next = None
        second = self.reverse(second)
        self.merge(head, second)
