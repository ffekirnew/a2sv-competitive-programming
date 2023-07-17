from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def reverse_linked_list(linked_list: ListNode) -> ListNode:
        prev_node = None
        curr_node = linked_list

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numbers: List[ListNode] = []

        # reverse both numbers
        for linked_list in [l1, l2]:
            numbers.append(self.reverse_linked_list(linked_list))
            
        
        # Create a new linked list to contain the answer and do elementary addition on it
        answer: ListNode = ListNode()
            
        curr_index = answer
        carry_over = 0

        number1, number2 = numbers
        while number1 or number2:
            curr_sum = carry_over
            if number1:
                curr_sum += number1.val
                number1 = number1.next
            if number2:
                curr_sum += number2.val
                number2 = number2.next
            
            carry_over = curr_sum // 10
            curr_sum %= 10
            
            curr_index.val = curr_sum
            curr_index.next = ListNode()
            curr_index = curr_index.next
        
        if carry_over:
            curr_index.val = carry_over
            curr_index.next = ListNode()
            curr_index = curr_index.next
        
        return self.reverse_linked_list(answer).next
                
        