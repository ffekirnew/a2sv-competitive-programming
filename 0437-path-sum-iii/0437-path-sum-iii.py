# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backtrack(self, curr_sum, node):
        if not node:
            return

        curr_sum += node.val
        if curr_sum - self.targetSum in self.prefix:
            self.answers += self.prefix[curr_sum - self.targetSum]
        self.prefix[curr_sum] += 1
        self.backtrack(curr_sum, node.left)
        self.backtrack(curr_sum, node.right)
        self.prefix[curr_sum] -= 1
        curr_sum -= node.val

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.prefix = defaultdict(int)
        self.prefix[0] += 1
        self.targetSum = targetSum
        self.answers = 0
        # do some
        self.backtrack(0, root)
        
        return self.answers
        