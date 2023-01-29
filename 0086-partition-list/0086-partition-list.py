# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser_nodes = None
        curr_lesser = None
        
        other_nodes = None
        curr_other = None
        
        while head:
            
            temp = ListNode(head.val)
            if head.val < x:
                
                if not lesser_nodes:
                    lesser_nodes = temp
                    curr_lesser = lesser_nodes
                else:
                    curr_lesser.next = temp
                    curr_lesser = temp
                    
            else:
                
                if not other_nodes:
                    other_nodes = temp
                    curr_other = other_nodes
                    
                else:
                    curr_other.next = temp
                    curr_other = temp
                    
            head = head.next
            
        if curr_lesser:
            curr_lesser.next = other_nodes
        else:
            lesser_nodes = other_nodes
        
        return lesser_nodes
        