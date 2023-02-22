# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, array, node: Optional[TreeNode]) -> None:
        if node:
            array.append(node.val)
            self.traverse(array, node.left)
            self.traverse(array, node.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        all_nums = []
        self.traverse(all_nums, root)
        
        all_nums.sort()
        
        minimum = float('inf')
        for i in range(1, len(all_nums)):
            minimum = min( minimum, all_nums[i] - all_nums[i - 1] )
        
        return minimum
            
        