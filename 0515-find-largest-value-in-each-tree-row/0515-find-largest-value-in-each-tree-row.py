# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        
        def traverse(node=root, level=0):
            if not node:
                return

            if level == len(answer):
                answer.append(node.val)
            else:
                answer[level] = max( answer[level], node.val )
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        
        traverse()
        
        return answer
        