# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backtrack(self, curr_sum, node):
        if not node:
            return
        if not node.right and not node.left:
            return (curr_sum + node.val) == (self.targetSum)
            
        curr_sum += node.val
        if self.backtrack(curr_sum, node.left):
            return True
        if self.backtrack(curr_sum, node.right):
            return True
        curr_sum -= node.val
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum = targetSum
        
        return self.backtrack(0, root)
        
        
        