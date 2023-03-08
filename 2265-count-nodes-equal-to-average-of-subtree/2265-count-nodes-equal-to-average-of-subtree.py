# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode], isRoot: bool = True) -> int:
        if not root:
            return tuple([0, 0, 0])
        
        left_sum, left_num_nodes, left_count = self.averageOfSubtree(root.left, False)
        right_sum, right_num_nodes, right_count = self.averageOfSubtree(root.right, False)
        
        total_sum = right_sum + left_sum + root.val
        num_nodes = left_num_nodes + right_num_nodes + 1
        average = total_sum // num_nodes
        count = left_count + right_count + (1 if average == root.val else 0)
        
        if isRoot:
            return count
        return tuple([ total_sum, num_nodes, count ])
