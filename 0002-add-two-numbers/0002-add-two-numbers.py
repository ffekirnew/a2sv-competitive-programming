# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create the object to be returned
        answer = ListNode()
        # create a pointer to keep track of digit and spill_overs
        curr_digit = answer
        carry = 0
        # loop through the solution and add
        while (l1 or l2):
            dig1 = l1.val if l1 else 0
            l1 = l1.next if l1 else None
            dig2 = l2.val if l2 else 0
            l2 = l2.next if l2 else None

            curr_sum = dig1 + dig2 + carry
            curr_digit.next  = ListNode(curr_sum % 10)
            carry = curr_sum // 10

            curr_digit = curr_digit.next

        # take care of any reserve carries
        curr_digit.next = ListNode(carry) if (carry) else None
        # return the solution
        return answer.next        