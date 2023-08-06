class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def has_cycle(in_degree: List[int], graph: List[List[int]]) -> bool:
            indegree = in_degree.copy()
            queue =  [node for node in range(1, k + 1) if indegree[node] == 0]
            nodes_seen = 0
            
            while queue:
                node = queue.pop()
                nodes_seen += 1

                for child in graph[node]:
                    indegree[child] -= 1
                    
                    if not indegree[child]:
                        queue.append(child)

            return nodes_seen != k

        def build_dependency_graph(conditions: List[List[int]]) -> List[List[int]]:
            graph = [[] for _ in range(k + 1)]
            indegree = [0 for _ in range(k + 1)]
            for before, after in conditions:
                graph[before].append(after)
                indegree[after] += 1
            
            return graph, indegree

        row_graph, row_indegree = build_dependency_graph(rowConditions)
        col_graph, col_indegree = build_dependency_graph(colConditions)
        
        if has_cycle(row_indegree, row_graph) or  has_cycle(col_indegree, col_graph):
            return []
        
        # Arrange them by column
        result = [[0 for _ in range(k)] for __ in range(k)]
        col = 0
        columns = {}
        
        queue = [node for node in range(1, k + 1) if col_indegree[node] == 0]
        while queue:
            num = queue.pop()
            result[0][col] = num
            columns[num] = col
            col += 1
            
            for next_ in col_graph[num]:
                col_indegree[next_] -= 1
                
                if not col_indegree[next_]:
                    queue.append(next_)
        
        # Arrange them by column
        row = 0
        queue = [node for node in range(1, k + 1) if row_indegree[node] == 0]
        while queue:
            num = queue.pop()
            result[row][columns[num]], result[0][columns[num]] = result[0][columns[num]], result[row][columns[num]]
            row += 1
            
            for next_ in row_graph[num]:
                row_indegree[next_] -= 1
                
                if not row_indegree[next_]:
                    queue.append(next_)
        
        
        return result
    
        