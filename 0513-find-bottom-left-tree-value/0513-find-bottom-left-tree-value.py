# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        root_level = deque([root]) if root else None
        
        while root_level:
            answer.append([])
            next_level = deque([])
            
            while root_level:
                node = root_level.popleft()

                answer[-1].append(node.val if node else "None")
                if node:
                    next_level.append(node.left) if node.left else None
                    next_level.append(node.right) if node.right else None

            root_level = next_level
        
        return answer
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.levelOrder(root)[-1][0]
        