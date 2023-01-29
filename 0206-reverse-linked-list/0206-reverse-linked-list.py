# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        curr = None
        
        while head:
            if not curr:
                new_head = ListNode(head.val)
                curr = new_head
            else: 
                temp = ListNode(head.val)
                temp.next = curr
                curr = temp
            head = head.next
        
        return curr
        