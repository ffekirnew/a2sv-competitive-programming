# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        answer = [0]
        
        # do something
        def dfs(node, parent, grand_parent):
            if not node:
                return
            
            if grand_parent and grand_parent.val % 2 == 0:
                answer[0] += node.val
            
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)            
            
        
        dfs(root, None, None)
        return answer[0]
        