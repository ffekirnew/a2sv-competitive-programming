# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        # create the object to be returned
        answer = ListNode()
        curr_node = answer
        # loop through the lists like in the merging part of merge sort (with two pointers)
        while (l1 and l2):
            if l1.val < l2.val: curr_node.next, l1 = l1, l1.next
            else: curr_node.next, l2 = l2, l2.next

            curr_node = curr_node.next
        curr_node.next = l2 if (l1 is None) else l1
        return answer.next

    def mergeKLists(self, lists: Optional[ListNode]) -> Optional[ListNode]:
        # if the length of the array is less than zero
        if len(lists) < 1: 
            return None
        
        # just use merge sort
        index = len(lists) - 1
        while index > 0:
            i, j = 0, index
            while i < j:
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                index = j

        # return the last element in the list
        return lists[0]