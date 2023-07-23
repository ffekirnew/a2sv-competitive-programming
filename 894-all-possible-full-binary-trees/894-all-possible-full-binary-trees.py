# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {1: [TreeNode()]}
        def dp(n):
            if n % 2 == 0:
                return []

            if n not in memo:
                memo[n] = []
                
                for left_nodes in range(1, n, 1):
                    for possible_left in dp(left_nodes):
                        for possible_right in dp(n - left_nodes - 1):
                            memo[n].append(TreeNode(0, possible_left, possible_right))                           
            
            return memo[n]
        
        return dp(n)
                        
        
        
        