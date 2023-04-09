class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, group=True):
            if node in visited:
                return
            
            bi_partite[node] = group
            visited.add(node)
            
            for child in graph[node]:
                if child not in visited:
                    dfs(child, not group)
            
            
        graph = defaultdict(set)
        
        for dislike in dislikes:
            graph[dislike[0]].add(dislike[1])
            graph[dislike[1]].add(dislike[0])
        
        bi_partite = {}
        visited = set()
        for i in range(1, n + 1):
            dfs(i)
        
        for dislike in dislikes:
            if bi_partite[dislike[0]] is bi_partite[dislike[1]]:
                return False
        
        return True
            