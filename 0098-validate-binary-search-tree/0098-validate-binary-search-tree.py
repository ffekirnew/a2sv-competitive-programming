# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tree = []
        
        def traverseInOrder(root):
            if not root:
                return

            traverseInOrder(root.left)
            tree.append(root.val)
            traverseInOrder(root.right)
        
        traverseInOrder(root)
        
        for i in range(1, len(tree)):
            if tree[i] <= tree[i - 1]:
                return False
        
        return True
        