class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def dfs(curr, target):
            if curr[-1] == target:
                paths.append(curr)
                return
            
            for nextval in graph[curr[-1]]:
                dfs(curr + [nextval], target)

        dfs([0], len(graph) - 1)

        return paths

