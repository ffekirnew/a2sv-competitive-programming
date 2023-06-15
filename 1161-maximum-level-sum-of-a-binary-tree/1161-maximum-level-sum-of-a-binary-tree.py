# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = []
        
        root_level = [root]
        while root_level:
            levels.append([])
            children_level = []
            
            for node in root_level:
                levels[-1].append(node.val)
                
                if node.left:
                    children_level.append(node.left)
                
                if node.right:
                    children_level.append(node.right)
            
            root_level = children_level
        
        answer = 0
        maximal_sum = -inf
        
        for i, level in enumerate(levels):
            if sum(level) > maximal_sum:
                answer = i + 1
                maximal_sum = sum(level)
        
        return answer
        