# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # create a stack
        stack = []
        # iterate over the linked list
        while head:
            stack.append(head.val)
            head = head.next
        # create the two pointers
        i, j = 0, len(stack) - 1
        while i < j:
            if stack[i] != stack[j]:
                return False
            i += 1
            j -= 1
        return True