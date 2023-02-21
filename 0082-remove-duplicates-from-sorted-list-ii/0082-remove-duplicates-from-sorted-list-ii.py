# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a pointer
        to_be_removed = {}
        prev_node = None
        curr_node = head
        # loop through the head using two pointers
        while curr_node:
            if curr_node.val in to_be_removed:
                if prev_node:
                    prev_node.next = curr_node.next
                    curr_node = prev_node.next
                else:
                    head = head.next
                    curr_node = head
            else:
                if curr_node.next and curr_node.val == curr_node.next.val:
                    to_be_removed[curr_node.val] = 1
                else:
                    prev_node = curr_node
                    curr_node = curr_node.next
        # return back the head
        return head
        