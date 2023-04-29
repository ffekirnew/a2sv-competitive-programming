# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        fringe = [(root, 0)] if root else []
        next_level = []
        
        latest_level = fringe
        
        while fringe:
            next_level = []
            
            for node, level in fringe:
                if node.left:
                    next_level.append((node.left, level + 1))
                if node.right:
                    next_level.append((node.right, level + 1))
                    
            latest_level = fringe
            fringe = next_level

        return sum(node.val for node, level in latest_level)
                
            
            
            
        