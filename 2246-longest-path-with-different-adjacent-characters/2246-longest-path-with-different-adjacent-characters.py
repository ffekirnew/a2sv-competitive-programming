class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        answer = [0]
        
        for i, node in enumerate(parent):
            graph[node].append(i)
        
        def dfs(node):
            longest, second = 0, 0
            for child in graph[node]:
                child_path = dfs(child)
                
                if s[node] != s[child]:
                    
                    if child_path >= longest:
                        longest, second = child_path, longest
                    else:
                        second = max(second, child_path)
            
            answer[0] = max(1 + longest + second, answer[0])
            
            return longest + 1
                    
        dfs(0)
        return answer[0]
