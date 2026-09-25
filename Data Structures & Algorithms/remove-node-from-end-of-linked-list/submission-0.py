# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        node = head
        while node != None:
            sz += 1
            node = node.next
        
        if sz - n == 0:
            return head.next

        i = 0
        prev = None
        node = head
        while node != None:
            if i == sz - n:
                prev.next = node.next
            prev = node
            node = node.next
            i += 1

        return head