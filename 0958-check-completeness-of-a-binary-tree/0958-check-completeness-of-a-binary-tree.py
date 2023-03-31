# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        root_level = [root]
        
        while root_level:
            answer.append([])
            children_level = []
            for node in root_level:
                answer[-1].append(node.val if node else None)
                if node:
                    children_level.append(node.left if node.left else None)
                    children_level.append(node.right if node.right else None)
            root_level = children_level
        return answer
    
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        level_order = self.levelOrder(root)
        
        none_is_found_in_upper_level = False
        for i, level in enumerate(level_order):
            none_is_found_in_same_level = False
            for val in level:
                if (none_is_found_in_upper_level or none_is_found_in_same_level) and val != None:
                    return False
                elif val == None:
                    none_is_found_in_same_level = True

            if none_is_found_in_same_level:
                none_is_found_in_upper_level = True
        
        return True
        