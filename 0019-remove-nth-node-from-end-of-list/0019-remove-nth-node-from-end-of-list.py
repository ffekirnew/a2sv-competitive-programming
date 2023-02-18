# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create two pointers
        before_turtle = None
        hare, turtle = head, head
        hare_ind, turtle_ind = 0, 0
        # loop through the ListNode keeping n distance between the hare and the turtle
        while hare:
            hare = hare.next
            hare_ind += 1
            if hare_ind - turtle_ind > n:
                before_turtle = turtle
                print(before_turtle.val, turtle.val)
                turtle = turtle.next
                turtle_ind += 1
        # delete the turtle
        if turtle == head:
            return head.next
        elif before_turtle: 
            before_turtle.next = turtle.next
        # return the head back
        return head if before_turtle else None