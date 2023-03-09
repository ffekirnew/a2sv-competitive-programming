# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def splitNode(head: Optional[ListNode]) -> [Optional[ListNode], Optional[ListNode]]:
        # create two pointers
        left = head
        prev = None
        right = head
        
        while right and right.next:
            prev = left
            left = left.next
            right = right.next.next
        
        prev.next = None
        return head, left

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if not left:
            return right
        elif not right:
            return left
        else:
            head = None
            
            if left.val < right.val:
                head = ListNode(left.val)
                head.next = self.merge(left.next, right)
            else:
                head = ListNode(right.val)
                head.next = self.merge(right.next, left)
            
            return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left, right = self.splitNode(head)
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
        