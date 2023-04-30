# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
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

        # Do the bfs and collect the answer nodes
        answer = []
        
        queue = deque([(target.val, 0)])
        visited = set([target.val])
        
        while queue:
            curr_node, path_length = queue.popleft()
            
            if path_length == k:
                answer.append(curr_node)
                continue
            
            for child in graph[curr_node]:
                if child not in visited:
                    visited.add(child)
                    queue.append((child, path_length + 1))
                
        
        return answer
            
        