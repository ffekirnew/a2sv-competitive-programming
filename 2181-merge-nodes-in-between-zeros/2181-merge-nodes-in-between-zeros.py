# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        last = None
        while current.next:
            last = current
            if current.next.val:
                current.val += current.next.val
                current.next = current.next.next
            else:
                current = current.next
        last.next = None
        return head
        