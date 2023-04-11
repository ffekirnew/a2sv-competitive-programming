class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        is_goal_node = lambda x: x == len(graph) - 1
        
        def dfs(start):
            answer = []
            fringe = []

            fringe.append([start, [start]])

            while fringe:
                curr_node, curr_path = fringe.pop()

                if is_goal_node(curr_node):
                    answer.append(curr_path.copy())
                    continue
                    
                for node in graph[curr_node]:
                    fringe.append((node, curr_path + [node]))
            
            return answer
        
        return dfs(0)

            
        