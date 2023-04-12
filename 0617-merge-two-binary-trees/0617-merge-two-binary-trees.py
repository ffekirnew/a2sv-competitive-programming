class Solution(object):
    def mergeTrees(self, root1, root2):
        def constructTree(root1, root2):
            if not (root1 or root2):
                return

            if not root2:
                return root1

            if not root1:
                return root2

            head = TreeNode(root1.val + root2.val)
            head.left = constructTree(root1.left, root2.left)
            head.right = constructTree(root1.right, root2.right)
        
            return head
        
        return constructTree(root1, root2)