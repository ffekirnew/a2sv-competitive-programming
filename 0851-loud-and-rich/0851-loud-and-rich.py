from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(set)
        in_coming = defaultdict(int)
        
        for from_, to_ in richer:
            graph[from_].add(to_)
            in_coming[to_] += 1
        
        queue = deque([node for node in range(len(quiet)) if not in_coming[node]])
        answer = [i for i in range(len(quiet))]
        while queue:
            node = queue.popleft()
            
            for child in graph[node]:
                if quiet[node] <= quiet[child]:
                    quiet[child] = min(quiet[child], quiet[node])
                    answer[child] = answer[node]
                    
                in_coming[child] -= 1
                
                if not in_coming[child]:
                    queue.append(child)
        
        return answer
        
        
        
        