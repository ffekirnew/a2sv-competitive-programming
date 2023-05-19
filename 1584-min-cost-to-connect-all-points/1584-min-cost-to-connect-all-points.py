class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def __contains__(self, x):
        return x in self.parent
        

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        stack = []
        while self.parent[x] != x:
            stack.append(x)
            x = self.parent[x]

        # Path compression
        for node in stack:
            self.parent[node] = x

        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


class Solution:
    @staticmethod
    def manhattanDistance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                graph.append((self.manhattanDistance(points[i], points[j]), tuple(points[i]), tuple(points[j])))
        
        graph.sort()
        
        points = UnionFind()
        total_cost = 0
        
        for cost, p1, p2 in graph:
            if p1 not in points or p2 not in points or points.find(p1) != points.find(p2):
                total_cost += cost
                
                points.make_set(p1)
                points.make_set(p2)
                points.union(p1, p2)
        
        return total_cost
                
                
        