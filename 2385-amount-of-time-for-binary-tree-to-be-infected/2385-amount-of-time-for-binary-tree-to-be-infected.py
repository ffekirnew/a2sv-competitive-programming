# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        
        # Build the graph to search from
        nodes = deque([root]) if root else []
        while nodes:
            root = nodes.popleft()
            
            left = root.left
            right = root.right
            
            if left:
                graph[root.val].append(left.val)
                graph[left.val].append(root.val)
                nodes.append(left)
            
            if right:
                graph[root.val].append(right.val)
                graph[right.val].append(root.val)
                nodes.append(right)
        
        time = 0
        
        # do the bfs
        queue = deque([(start, 0)])
        visited = set([start])
        
        while queue:
            curr_node, time = queue.popleft()
            
            for child in graph[curr_node]:
                if child not in visited:
                    visited.add(child)
                    queue.append([child, time + 1])
        
        return time
        