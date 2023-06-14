# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        list_ = []
        def in_order(node):
            if not node:
                return
            
            list_.append(node.val)
            in_order(node.left)
            in_order(node.right)
            
        in_order(root)
        list_.sort()
        min_ = inf
        for i in range(len(list_) - 1):
            min_ = min(min_, abs(list_[i] - list_[i + 1]))
        
        return min_
            
            
        