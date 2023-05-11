from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for num1, num2 in adjacentPairs:
            graph[num1].append(num2)
            graph[num2].append(num1)
            in_degree[num1] += 1
            in_degree[num2] += 1
        
        stack = [node for node in graph.keys() if in_degree[node] == 1][:1]
        visited = set()
        answer = []

        while stack:
            node = stack.pop()

            visited.add(node)
            answer.append(node)

            for child in graph[node]:
                if child not in visited:
                    stack.append(child)
        
        return answer