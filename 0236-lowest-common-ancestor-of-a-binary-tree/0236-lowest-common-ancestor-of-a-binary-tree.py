# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class LowestCommonAncestorOfABinaryTree:
    def __init__(self, root: 'TreeNode', p: int, q: int):
        self.root = root
        self.p = p
        self.q = q

    def find_lowers_common_ancestor_of_a_binary_tree(self) -> 'TreeNode':
        answer = [None]

        def dfs(node: 'TreeNode') -> bool:
            if not node or answer[0] != None:
                return None

            left, right = dfs(node.left), dfs(node.right)
            if left is not None and right is not None:
                answer[0] = node
            
            if left is not None or right is not None:
                if node.val in [self.p, self.q]:
                    answer[0] = node
                elif left is not None:
                    return left
                return right

            if node.val in [self.p, self.q]:
                return node.val

            return None
        
        dfs(self.root)
        return answer[0]
                

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        solution = LowestCommonAncestorOfABinaryTree(root, p.val, q.val)
        return solution.find_lowers_common_ancestor_of_a_binary_tree()