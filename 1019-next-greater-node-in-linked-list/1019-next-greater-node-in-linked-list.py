# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # create the object to be returned
        answer: List[int] = []
        # create a stack to be used as a monotonic stack
        stack = []
        # loop through the linked list
        i = 0
        while head:
            answer.append(0)
            while stack and stack[-1][0] < head.val:
                answer[stack.pop()[1]] = head.val
            stack.append([head.val, i])
            head = head.next
            i += 1
                    
        # return the solution
        return answer
        