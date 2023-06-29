# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        level = {}
        parent = {}
        
        def dfs(node, depth, node_parent):
            if not node:
                return
            
            level[node.val] = depth
            parent[node.val] = node_parent
            dfs(node.left, depth + 1, node.val)
            dfs(node.right, depth + 1, node.val)
        
        dfs(root, 0, -1)
        
        return level[x] == level[y] and parent[x] != parent[y]
        