# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kth_from_beggining = None
        turtle = head
        hare = head
        index = 1
        
        while hare:
            if index == k:
                kth_from_beggining = hare
            if index > k:
                turtle = turtle.next

            hare = hare.next
            index += 1
        
        if kth_from_beggining is None:
            kth_from_beggining = head
        
        kth_from_beggining.val, turtle.val = turtle.val, kth_from_beggining.val
                
        
        return head
        