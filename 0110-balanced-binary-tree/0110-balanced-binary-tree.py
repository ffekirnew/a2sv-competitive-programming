# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        depth = lambda node: max( 1 + depth(node.left), 1 + depth(node.right) ) if node else 0
        
        return abs(depth(root.left) - depth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        