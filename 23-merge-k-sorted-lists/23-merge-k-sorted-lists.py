# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: Optional[ListNode]) -> Optional[ListNode]:
        # add all elements onto a heap
        heap = []
        for list in lists:
            curr = list
            
            while curr:
                heapq.heappush(heap, -1 * curr.val)
                curr = curr.next

        # pop them one by one
        answer = None
        while heap:
            node = ListNode(-1 * heapq.heappop(heap))
            node.next = answer
            answer = node
        
        return answer