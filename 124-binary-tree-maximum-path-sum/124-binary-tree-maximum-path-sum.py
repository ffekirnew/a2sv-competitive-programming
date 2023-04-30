# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = [-inf]
        def dfs(node):
            if not node:
                return 0
            
            val = node.val
            left = dfs(node.left)
            right = dfs(node.right)
            
            max_sum = max(val, val + left, val + right, val + right + left)
            max_side = max(val, val + left, val + right)
            
            answer[0] = max(max_sum, answer[0])
            
            return max_side
                    
        dfs(root)
        return answer[0]
        