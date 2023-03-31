# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        node = TreeNode(preorder[0])
        
        for index in range(1, len(preorder)):
            self.insertIntoBST(node, preorder[index])
        
        return node
        