# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, node, array=[]):
        if not node:
            return

        if not node.left and not node.right:
            array.append(str(node.val) if not array else "->" + str(node.val))
            self.binary_paths.append("".join(array))
            array.pop()
            return
            
        
        array.append(str(node.val) if not array else "->" + str(node.val))
        self.rec(node.left, array)
        self.rec(node.right, array)
        array.pop()
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # create the object to be returned
        self.binary_paths = []
        
        # do something
        self.rec(root)
        
        # return the solution
        return self.binary_paths
        