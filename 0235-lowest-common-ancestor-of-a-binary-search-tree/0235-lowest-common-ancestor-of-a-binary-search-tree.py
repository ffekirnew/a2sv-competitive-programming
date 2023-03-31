# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_ancestors(node, key, answer):
            answer.append(node)
            
            if node.val == key:
                return answer
            
            if node.val < key:
                return get_ancestors(node.right, key, answer)
            
            return get_ancestors(node.left, key, answer)
            
        p_ancestors = get_ancestors(root, p.val, [])
        q_ancestors = get_ancestors(root, q.val, [])
        
        for i in range(min( len(p_ancestors), len(q_ancestors) )):
            if p_ancestors[i] != q_ancestors[i]:
                return p_ancestors[i - 1]
            
        
        if len(p_ancestors) < len(q_ancestors):
            return p_ancestors[-1]
        return q_ancestors[-1]
        
        