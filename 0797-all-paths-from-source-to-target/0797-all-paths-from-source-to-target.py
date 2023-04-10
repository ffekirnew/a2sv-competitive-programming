class Solution:
    @staticmethod
    def buildGraph(adj_list: list[list[int]]):
        return {i: set(children) for i, children in enumerate(adj_list)}
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        graph = self.buildGraph(graph)
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

            
        