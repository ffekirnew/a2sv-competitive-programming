# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create the object to be returned
        answer = ListNode()
        curr_node = answer
        # loop through the lists like in the merging part of merge sort (with two pointers)
        while (list1 and list2):
            if list1.val < list2.val: curr_node.next, list1 = list1, list1.next
            else: curr_node.next, list2 = list2, list2.next
            
            curr_node = curr_node.next
        curr_node.next = list2 if (list1 is None) else list1
        return answer.next
        