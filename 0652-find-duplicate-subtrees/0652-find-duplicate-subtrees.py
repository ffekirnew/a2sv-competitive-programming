# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindDuplicateSubtrees:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        
    
    def solve(self):
        result = {}

        nodes = defaultdict(int)
        def dfs(node):
            if node is None:
                return ""
            
            left = dfs(node.left)
            if not left:
                left = '><'

            right = dfs(node.right)
            if not right:
                right = '><'

            string_representation = '>' + str(node.val) + '<' + left + right
            nodes[string_representation] += 1

            if nodes[string_representation] > 1:
                result[string_representation] = node
                
            return string_representation
        
        dfs(self.root)
        
        return list(result.values())


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        solution = FindDuplicateSubtrees(root)
        return solution.solve()
        
        
        
        