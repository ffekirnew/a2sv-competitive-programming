class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_order = {val: index for index, val in enumerate(postorder)}
        in_order = {val: index for index, val in enumerate(inorder)}
        
        stack = []
        root = TreeNode(postorder[-1])
        stack.append((root, 0, len(inorder) - 1))
        
        while stack:
            node, in_start, in_end = stack.pop()
            post_val = post_order[node.val]
            in_index = in_order[node.val]
            
            if in_index > in_start:
                left_node = TreeNode(postorder[post_val - (in_end - in_index) - 1])
                node.left = left_node
                stack.append((left_node, in_start, in_index - 1))
                
            if in_index < in_end:
                right_node = TreeNode(postorder[post_val - 1])
                node.right = right_node
                stack.append((right_node, in_index + 1, in_end))
                
        return root
