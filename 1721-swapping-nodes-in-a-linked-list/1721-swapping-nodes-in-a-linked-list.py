# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kth_from_beggining = None
        kth_from_end = head
        end = head
        index = 1
        
        while end is not None:
            if index == k:
                kth_from_beggining = end
            if index > k:
                kth_from_end = kth_from_end.next

            end = end.next
            index += 1
        
        if kth_from_beggining is None:
            kth_from_beggining = head
        
        kth_from_beggining.val, kth_from_end.val = kth_from_end.val, kth_from_beggining.val
                
        
        return head
        