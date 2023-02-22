# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create two pointers
        first = head
        first_ind = 0
        second = head
        second_ind = 0
        # loop through the
        while first:
            first = first.next
            first_ind += 1
            midway = first_ind // 2
            while second_ind < midway:
                second_ind += 1
                second = second.next
        # return the halfway
        return second