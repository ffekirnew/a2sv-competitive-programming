# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        answer = []
        
        # do somthing
        def pre_order(node, is_root=False):
            if not node:
                return False
            
            if not is_root:
                answer.append("(")
            answer.append(str(node.val))
            left_exists = node.left != None
            right_exists = node.right != None
            
            if not left_exists and right_exists:
                answer.append("()")
            
            pre_order(node.left)
            pre_order(node.right)
            
            if not is_root:
                answer.append(")")
            
            return True
        
        pre_order(root, True)
        return "".join(answer)