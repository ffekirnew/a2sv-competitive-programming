# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order_list = []
        
        def traverseInOrder(root):
            if not root:
                return

            traverseInOrder(root.left)
            in_order_list.append(root.val)
            traverseInOrder(root.right)
        
        traverseInOrder(root)
        return in_order_list[k - 1]
            
            
        