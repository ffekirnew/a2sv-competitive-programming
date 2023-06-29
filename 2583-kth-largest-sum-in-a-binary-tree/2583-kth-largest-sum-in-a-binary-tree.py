import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        root_level = [root]
        
        while root_level:
            level_sum = -1
            children_level = []
            
            for root in root_level:
                if not root:
                    continue
                level_sum += root.val + (1 if level_sum == -1 else 0)
                children_level.append(root.left)
                children_level.append(root.right)
            
            root_level = children_level
            heapq.heappush(level_sums, -level_sum)
        
        if not k <= len(level_sums):
            return -1
        
        while k - 1:
            heapq.heappop(level_sums)
            k -= 1
        
        return -level_sums[0]
        