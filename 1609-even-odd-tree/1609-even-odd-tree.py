# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_traversal = []
        root_level = [root] if root else None
        
        while root_level:
            level_order_traversal.append([])
            next_level = []
            
            for node in root_level:
                level_order_traversal[-1].append(node.val if node else "None")
                if node:
                    next_level.append(node.left) if node.left else None
                    next_level.append(node.right) if node.right else None

            root_level = next_level
        
        return level_order_traversal
    
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level_order = self.levelOrder(root)
        
        for i in range(len(level_order)):
            if i % 2 == 0:
                for j in range(len(level_order[i])):
                    if level_order[i][j] % 2 == 0:
                        return False
                    if j > 0 and level_order[i][j] <= level_order[i][j - 1]:
                        return False
            else:
                for j in range(len(level_order[i])):
                    if level_order[i][j] % 2 == 1:
                        return False
                    if j > 0 and level_order[i][j] >= level_order[i][j - 1]:
                        return False
        
        return True

        