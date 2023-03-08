# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        vals = []

        def inOrderTraversal(root, level = [0, 0]):
            if not root:
                return
            
            inOrderTraversal(root.left, [level[0] + 1, level[1] - 1])
            vals.append([root.val, level])
            inOrderTraversal(root.right, [level[0] + 1, level[1] + 1])
        
        inOrderTraversal(root)
        
        vals.sort(key=lambda x: x[1][1])
        
        answer = [[]]
        for i, val in enumerate(vals):
            if not answer[-1]:
                answer[-1].append(val)
            else:
                if val[1][1] > vals[i - 1][1][1]:
                    answer.append([])
                answer[-1].append(val)

        for i, vertical in enumerate(answer):
            answer[i].sort(key=lambda x: [x[1], x[0]])
            answer[i] = [value[0] for value in vertical]

        return answer