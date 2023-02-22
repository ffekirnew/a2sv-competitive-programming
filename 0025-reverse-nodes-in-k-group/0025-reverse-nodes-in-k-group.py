# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addToNodeTail(self, head: Optional[ListNode], val: any):
        if head:
            curr = head
            
            while curr and curr.next:
                curr = curr.next
            curr.next = ListNode(val) if isinstance(val, int) else val
            
            return head

        return ListNode(val)

    def addToNodeHead(self, head: Optional[ListNode], val: int):
        return ListNode(val, head if head else None)
    
    def reverseNode(self, head):
        answer = None
        while head:
            answer = self.addToNodeHead(answer, head.val)
            head = head.next
        print(answer)
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # create the object to be returned
        segments = []
        last_is_okay = True
        # segment the given in segments of k
        while head:
            segments.append(None)
            
            idx = 0
            while idx < k and head:
                segments[-1] = self.addToNodeTail(segments[-1], head.val)
                head = head.next
                idx += 1
            
            if idx != k:
                last_is_okay = False

        # reverse the segments
        for i in range(len(segments)):
            if i == len(segments) - 1 and not last_is_okay:
                break
            
            temp = None
            head = segments[i]
            while head:
                temp = self.addToNodeHead(temp, head.val)
                head = head.next
            segments[i] = temp
        # link them together
        while len(segments) > 1:
            last = segments.pop()
            second_last = segments.pop()
            
            segments.append( self.addToNodeTail(second_last, last) )
            
        # return the solution
        return segments[0]
        