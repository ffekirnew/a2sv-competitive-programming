# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # create and initialize the object to be returned
        answer = 0
        # declare and initialize an empty doubly ended queue
        d = deque()
        # while head:
        while head:
            # append to doubly ended queue
            d.append(head.val)
            head = head.next
        # while deque:
        while d:
            # pop from left and right add them, keep the maximum
            answer = max(answer, d.popleft() + d.pop())
        # return the solution
        return answer
        