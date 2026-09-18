# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []
        node = head
        while node != None:
            nodes.append(node)
            node = node.next
        
        l = 0
        r = len(nodes) - 1
        node = head
        while l < r:
            node.next = nodes[r]
            node = node.next
            l += 1
            if l >= r:
                break
            node.next = nodes[l]
            node = node.next
            r -= 1
            
        node.next = None