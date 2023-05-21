class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        
        for from_, to_ in edges:
            graph[from_].append(to_)
            degree[from_] += 1
            
            graph[to_].append(from_)
            degree[to_] += 1
        
        answer = []
        leaf_level = deque([i for i in range(n) if degree[i] <= 1])
        graph_items = n
        
        while leaf_level:
            root_level = []
            
            for leaf in leaf_level:
                for root in graph[leaf]:
                    degree[root] -= 1
                    
                    if degree[root] == 1:
                        root_level.append(root)
            
            answer = leaf_level
            leaf_level = root_level
        
        return answer
                
        