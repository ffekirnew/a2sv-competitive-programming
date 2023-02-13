# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = head
        evens = head.next if head else None
        
        curr_even = evens
        curr_odd = odds
        
        while curr_odd and curr_even and curr_odd.next and curr_even.next:
            curr_odd.next = curr_odd.next.next
            curr_even.next = curr_even.next.next
            
            curr_odd = curr_odd.next
            curr_even = curr_even.next
        
        if curr_odd:
            curr_odd.next = evens
        
        return odds
            
            
        