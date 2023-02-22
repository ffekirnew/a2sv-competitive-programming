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

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # convert the linked list into three segments
        index = 1
        start_node = None
        middle_node = None
        end_node = None
        
        while index < left:
            start_node = self.addToNodeTail(start_node, head.val)
            head = head.next
            index += 1
        
        while index <= right:
            middle_node = self.addToNodeHead(middle_node, head.val)
            head = head.next
            index += 1
        
        while head:
            end_node = self.addToNodeTail(end_node, head.val)
            head = head.next
            
        # link all of them
        middle_node = self.addToNodeTail(middle_node, end_node) if middle_node else end_node
        start_node = self.addToNodeTail(start_node, middle_node) if start_node else middle_node
        

        # return the head
        return start_node
        
        