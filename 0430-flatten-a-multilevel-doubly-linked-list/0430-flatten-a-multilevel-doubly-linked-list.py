"""
Note:
- Can think of it as a separate data structure

Clarification Questions:
- How big can it be?
- 


Brute-force Solution Steps:
1. Assign the head to another dummy variable
2. Traverse the doubly-linked list
    2.1. If node doesn't have child, Continue
    2.2. If node has a child:
        2.2.1. Note the next node somewhere
        2.2.2. Traverse and find the inside doubly-linked list's end
        2.2.3. Point the next of the inside doubly-linked list to the original next node
        2.2.4. Point the next of the parent node to the start of the child node
        2.2.5. Set the child pointer of the parent node to null
3. Return the original head

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class FlattenAMultilevelDoublyLinkedList:
    def __init__(self, head: 'Optional[Node]'):
        self.head = head
    
    def brute_force(self) -> 'Optional[Node]':
        def flatten(node):
            if node is None:
                return node
            
            prev = None
            curr = node
            while curr:
                if curr.child:
                    end_of_inside_list = flatten(curr.child)
                    
                    original_next = curr.next
                    original_child = curr.child
                    
                    curr.next = original_child
                    end_of_inside_list.next = original_next
                    
                    if original_next:
                        original_next.prev = end_of_inside_list
                    original_child.prev = curr
                    
                    curr.child = None
                
                prev = curr
                curr = curr.next
            
            return prev
            
        flatten(self.head)
        return self.head


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        solution = FlattenAMultilevelDoublyLinkedList(head)
        return solution.brute_force()
        