# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        nodes = [root] if root else None
        
        while nodes:
            answer.append([])
            child_nodes = []
            for node in nodes:
                if node:
                    answer[-1].append(node.val)
                    child_nodes.append(node.left) if node.left else None
                    child_nodes.append(node.right) if node.right else None

            nodes = child_nodes
        
        return answer
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        level_order = self.levelOrder(root)
        
        for level in level_order:
            answer.append(level[-1])
        return answer
            