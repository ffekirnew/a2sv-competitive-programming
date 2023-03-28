# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None): 
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        
        level_order_list = []
        
        def level_order(root):
            root_level = [[root, 0]]
            
            while root_level:
                next_level = []
                level_order_list.append([])
                
                for curr in root_level:
                    if curr[0]:
                        level_order_list[-1].append(curr[1])
                        if curr[0].left:
                            next_level.append([curr[0].left, curr[1] * 2])
                        if curr[0].right:
                            next_level.append([curr[0].right, curr[1] * 2 + 1])
                
                root_level = next_level
        
        level_order(root)
        
        for level in level_order_list:
            if len(level) > 1:
                max_width = max(max_width, level[-1] - level[0] + 1)
            else:
                max_width = max(max_width, len(level))
                
        return max_width
                