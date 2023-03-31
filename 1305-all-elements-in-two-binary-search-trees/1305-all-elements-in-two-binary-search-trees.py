# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, list1, list2):
        answer = []

        i, j = 0, 0
        
        list1.append(inf)
        list2.append(inf)
        
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                answer.append(list1[i])
                i += 1
            else:
                answer.append(list2[j])
                j += 1
        
        answer.pop()
        
        return answer
                
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        in_order_root1 = []
        in_order_root2 = []
        
        def in_order_traversal(collector, node):
            if not node:
                return
            
            in_order_traversal(collector, node.left)
            collector.append(node.val)
            in_order_traversal(collector, node.right)
        
        in_order_traversal(in_order_root1, root1)
        in_order_traversal(in_order_root2, root2) 
        
        return self.merge(in_order_root1, in_order_root2)
                
        