# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        if first is None or first.next is None:
            return head
        
        second = head.next
        while second is not None:
            first.val, second.val = second.val, first.val
            
            if second.next is None or second.next.next is None:
                break
                
            first = second.next
            second = second.next.next
        
        return head
        