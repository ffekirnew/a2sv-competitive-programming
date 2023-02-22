# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, node: Optional[ListNode]):
        length = 0
        curr = node
        
        while curr:
            length += 1
            curr = curr.next
        
        return length
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            k = (self.length(head) - k) % self.length(head)
        
        if head and k:

            prev = None
            rest = head
            
            while rest and k > 0:
                prev = rest
                rest = rest.next
                k -= 1
            
            prev.next = None
            prev = head
            head = rest
            
            while rest.next:
                rest = rest.next
            
            rest.next = prev
            
        return head
        