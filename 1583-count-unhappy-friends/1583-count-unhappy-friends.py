class CountUnhappyFriends:
    def __init__(self, n: int, preferences: List[List[int]], pairs: List[List[int]]):
        self.n = n
        self.preferences = preferences
        self.pairs = pairs
    
    def _make_graph(self) -> Dict:
        friendship_graph = defaultdict(dict)
        
        for node, preference in enumerate(self.preferences):
            max_value = len(preference)
            
            for other_node in preference:
                friendship_graph[node][other_node] = max_value
                max_value -= 1
        
        return friendship_graph
    
    def solve(self):
        graph = self._make_graph()
        unhappy = set()
        
        for i in range(len(self.pairs)):
            for j in range(i + 1, len(self.pairs)):
                for k in range(2):
                    for l in range(2):
                        p1, p2 = self.pairs[i][k], self.pairs[i][1 - k]
                        p3, p4 = self.pairs[j][l], self.pairs[j][1 - l]

                        if graph[p1][p2] < graph[p1][p3] and graph[p3][p1] > graph[p3][p4]:
                            unhappy.add(p1)
                            unhappy.add(p3)
        return len(unhappy)

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        solution = CountUnhappyFriends(n, preferences, pairs)
        return solution.solve()
        