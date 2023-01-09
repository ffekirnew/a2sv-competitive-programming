# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre_order_list = []
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        current_node = root
        
        self.pre_order_list.append(current_node.val)
        if current_node.left:
            self.preorderTraversal(current_node.left)
        if current_node.right:
            self.preorderTraversal(current_node.right)
        
        return self.pre_order_list