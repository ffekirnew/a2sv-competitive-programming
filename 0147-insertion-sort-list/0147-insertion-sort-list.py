# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addToPlace(self, head: Optional[ListNode], val: int) -> None:
        if head:
            prev = None
            curr = head
            
            while curr and curr.val < val:
                prev = curr
                curr = curr.next
                
            if not prev:
                temp = ListNode(val)
                temp.next = curr
                head = temp
            else:
                prev.next = ListNode(val)
                prev.next.next = curr
                
        else:
            head = ListNode(val)
        
        return head

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start with an empty ListNode
        answer = None

        # pick all from the given head one by one
        while head:
            answer = self.addToPlace(answer, head.val)
            head = head.next

        # return the solution
        return answer
        