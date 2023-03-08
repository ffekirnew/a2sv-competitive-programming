# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        frequency = defaultdict(int)

        def freq_counter(node):
            if not node:
                return
            
            freq_counter(node.left)
            frequency[node.val] += 1
            freq_counter(node.right)
        
        freq_counter(root)
        
        sorted_freq = sorted(frequency.items(), key=lambda x: x[1])
        max_freq = sorted_freq[-1][1]
        
        answer = []
        while sorted_freq and sorted_freq[-1][1] == max_freq:
            answer.append( sorted_freq.pop()[0] )
        
        return answer
        
            
        