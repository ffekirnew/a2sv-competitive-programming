# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        root_level = [root] if root else None
        
        while root_level:
            answer.append([])
            next_level = []
            
            for node in root_level:
                answer[-1].append(node.val if node else "None")
                if node:
                    next_level.append(node.left) if node.left else None
                    next_level.append(node.right) if node.right else None

            root_level = next_level
        
        return answer
        