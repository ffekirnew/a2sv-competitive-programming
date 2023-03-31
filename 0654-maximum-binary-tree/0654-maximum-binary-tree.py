# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return
        
        maximum = max(nums)
        node = TreeNode(maximum)
        
        maximum_index = nums.index(maximum)
        node.left = self.constructMaximumBinaryTree(nums[:maximum_index])
        node.right = self.constructMaximumBinaryTree(nums[maximum_index + 1:])
        
        return node
        
        
        