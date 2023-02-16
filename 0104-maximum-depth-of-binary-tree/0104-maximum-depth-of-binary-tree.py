# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def left(self, node: Optional[TreeNode]) -> int:
        if node:
            return 1 + max(self.left(node.left), self.right(node.right))
        return 0
    def right(self, node: Optional[TreeNode]) -> int:
        if node:
            return 1 + max(self.left(node.left), self.right(node.right))
        return 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max(self.left(root), self.right(root))
        
        