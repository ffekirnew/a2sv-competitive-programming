# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # create a pointer
        prev_node = None
        curr_node = head
        # create a hashmap to keep track of frequencies
        freq_dict = {}
        # loop through the linked list
        while curr_node:
            if curr_node.val in freq_dict:
                prev_node.next = curr_node.next
            else:
                freq_dict[curr_node.val] = 1
                prev_node = curr_node
            curr_node = curr_node.next
        # return the new head
        return head
        
                
        