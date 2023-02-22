# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        turtle, hare = head, head
        
        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            
            if (hare == turtle):
                hare = head
                
                while turtle != hare:
                    turtle, hare = turtle.next, hare.next
                
                return turtle

        return None
        