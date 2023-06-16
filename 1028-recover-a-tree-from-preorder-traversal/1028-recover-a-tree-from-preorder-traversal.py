# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def addChild(parent_node, child_node):
        if not parent_node.left:
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels = defaultdict(list)
        
        curr_level, curr_number = 0, 0
        
        for i in range(len(traversal) + 1):
            char = traversal[i] if i < len(traversal) else '-'
            
            if '0' <= char <= '9':
                curr_number = curr_number * 10 + int(char)

            else:
                if curr_number:
                    levels[curr_level] = TreeNode(curr_number)
                    
                    if curr_level:
                        parent_node, curr_node = levels[curr_level - 1], levels[curr_level]
                        self.addChild(parent_node, curr_node)

                    curr_number, curr_level = 0, 0
                
                curr_level += 1

        return levels[0]
            
        