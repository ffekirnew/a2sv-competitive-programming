# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        nodes = deque([root]) if root else None
        
        while nodes:
            answer.append([])
            child_nodes = deque([])
            
            while nodes:
                node = nodes.popleft()

                answer[-1].append(node.val if node else None)
                if node:
                    child_nodes.append(node.left)
                    child_nodes.append(node.right)

            nodes = child_nodes
        
        return answer
    
    def isPalindrome(self, level):
        for i in range(len(level) // 2):
            if level[i] != level[len(level) - i - 1]:
                return False
        
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        level_order_traversal = self.levelOrder(root)
        
        return all( self.isPalindrome(level) for level in level_order_traversal )
        