# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backtrack(self, curr_sum, curr_arr, node):
        if not node:
            return
        if not (node.right) and (not node.left):
            if (curr_sum + node.val) == (self.targetSum):
                curr_arr.append(node.val)
                self.answers.append(curr_arr.copy())
                curr_arr.pop()
            return

        curr_sum += node.val
        curr_arr.append(node.val)
        self.backtrack(curr_sum, curr_arr, node.left)
        self.backtrack(curr_sum, curr_arr, node.right)
        curr_sum -= node.val
        curr_arr.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.targetSum = targetSum
        self.answers = []
        # do some
        self.backtrack(0, [], root)
        
        return self.answers