# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def returnMaxAndIndex(self, arr):
        maximum = max(arr)
        maximum_index = arr.index(maximum)
        
        return maximum, maximum_index

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return
        
        maximum, maximum_index = self.returnMaxAndIndex(nums)
        
        node = TreeNode(maximum)
        node.left = self.constructMaximumBinaryTree(nums[:maximum_index])
        node.right = self.constructMaximumBinaryTree(nums[maximum_index + 1:])
        
        return node
        
        
        