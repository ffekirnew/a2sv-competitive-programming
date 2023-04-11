# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, curr_num, node):
        if not node:
            return
        if not node.left and not node.right:
            self.nums.append(curr_num * 10 + node.val)
            return
        
        curr_num *= 10
        curr_num += node.val
        self.dfs(curr_num, node.left)
        self.dfs(curr_num, node.right)
        curr_num -= node.val
        curr_num //= 10
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        self.dfs(0, root)

        return sum(self.nums)