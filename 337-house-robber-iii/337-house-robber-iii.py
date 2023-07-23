# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(node):
            if not node:
                return 0

            if id(node) not in memo:
                robbing_the_house = node.val
                if node.right:
                    robbing_the_house += dp(node.right.left) + dp(node.right.right)
                if node.left:
                    robbing_the_house += dp(node.left.left) + dp(node.left.right)
                
                not_robbing_the_house = dp(node.left) + dp(node.right)

                memo[id(node)] = max(robbing_the_house, not_robbing_the_house)
            
            return memo[id(node)]
        
        return dp(root)
        