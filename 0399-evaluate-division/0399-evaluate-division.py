from collections import defaultdict


class EvaluageDivision:
    def __init__(self, equations: List[List[str]], values: List[float]):
        self.graph = defaultdict(list)
        
        for equation_index in range(len(equations)):
            variable1, variable2 = equations[equation_index]
            value = values[equation_index]
            
            self.graph[variable1].append((variable2, value))
            self.graph[variable2].append((variable1, 1 / value))
    
    def bfs(self, variable1: str, variable2: str) -> float:
        if variable1 not in self.graph or variable2 not in self.graph:
            return float(-1)
        
        value = 1
        queue = deque([(variable1, 1)])
        visited = set()
        
        while queue:
            next_queue = []
            
            for variable, value in queue:
                if variable == variable2:
                    return value

                if variable in visited:
                    continue
                
                visited.add(variable)
                
                for next_variable, division_value in self.graph[variable]:
                    next_queue.append((next_variable, value * division_value))

            queue = next_queue
        
        return -1


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        solution = EvaluageDivision(equations, values)
        
        result = []
        for variable1, variable2 in queries:
            result.append(solution.bfs(variable1, variable2))
        
        return result
        