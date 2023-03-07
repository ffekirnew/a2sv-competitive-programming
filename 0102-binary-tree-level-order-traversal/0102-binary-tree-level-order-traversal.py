# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        nodes = deque([root]) if root else None
        
        while nodes:
            answer.append([])
            child_nodes = deque([])
            
            while nodes:
                node = nodes.popleft()

                if node:
                    answer[-1].append(node.val)
                    child_nodes.append(node.left) if node.left else None
                    child_nodes.append(node.right) if node.right else None

            nodes = child_nodes
        
        return answer
        