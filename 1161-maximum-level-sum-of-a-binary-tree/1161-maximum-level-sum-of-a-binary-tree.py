# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        answer, maximal_sum = 0, -inf
        
        i = 1
        root_level = [root]
        while root_level:
            node_found_on_level = False
            level_sum, children_level = 0, []
            
            for node in root_level:
                if node:
                    node_found_on_level = True
                    level_sum += node.val
                    children_level.append(node.left)
                    children_level.append(node.right)
            
            if node_found_on_level and level_sum > maximal_sum:
                answer = i
                maximal_sum = level_sum
            
            i += 1
            root_level = children_level
        
        return answer
        