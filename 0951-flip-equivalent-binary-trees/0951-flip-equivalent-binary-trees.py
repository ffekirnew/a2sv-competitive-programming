# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Solution Steps:
1. Traverse the tree using two pointers
    1.1. On each step, compare the value of the roots
    1.2. Try fliping recursivelly, and Try non fliping recursively
    1.3. If one of the ways worked, return True
    
Complexity Analysis:
Time Complexity: O(n) - n = number of nodes
Space Complexity: O(n) - for the function call stack
"""
from typing import Optional


class FlipEquivalentBinaryTrees:
    def __init__(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        self.root1 = root1
        self.root2 = root2
    
    def dfs(self):
        def findEquivalentBinaryTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            # flip
            flipped = findEquivalentBinaryTrees(root1.left, root2.right) and findEquivalentBinaryTrees(root1.right, root2.left)

            # non-flipped
            non_flipped = findEquivalentBinaryTrees(root1.left, root2.left) and findEquivalentBinaryTrees(root1.right, root2.right)

            return root1.val == root2.val and (flipped or non_flipped)
        
        return findEquivalentBinaryTrees(self.root1, self.root2)


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        solution = FlipEquivalentBinaryTrees(root1, root2)
        return solution.dfs()