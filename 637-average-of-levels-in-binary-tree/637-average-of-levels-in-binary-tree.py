# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer = []
        fringe = [root] if root else []
        
        while fringe:
            answer.append(0)
            next_level = []
            
            for node in fringe:
                answer[-1] += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            answer[-1] /= len(fringe)
            fringe = next_level
        
        return answer
        
        