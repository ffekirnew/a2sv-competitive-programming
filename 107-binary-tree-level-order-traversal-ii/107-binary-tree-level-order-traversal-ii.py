# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        
        fringe = [root] if root else []
        
        while fringe:
            answer.append([])
            next_level = []
            
            for node in fringe:
                answer[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            fringe = next_level
        
        return reversed(answer)
        